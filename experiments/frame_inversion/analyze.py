"""
Frame-Inversion Test — analysis.

Unblinds the coded transcripts (joins codes back to conditions via key.jsonl),
tallies how often each feature appears per condition, and applies the FROZEN
decision rules from config.py (which mirror rubric.md). Prints a table and a
verdict: Supported / Undermined / Killed / Indeterminate.

This is the only step that re-attaches condition labels to codes. By the time it
runs, the coding is already done and sealed — opening the key here can't bias it.

USAGE
  /opt/anaconda3/bin/python analyze.py [--run runs/<stamp>]
  (defaults to the most recent run with a codes_haiku.jsonl)
"""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

import config

FEATURES = ["f1", "f2", "f3", "f4", "f5"]


def latest_run_dir() -> Path:
    runs = sorted(p for p in config.RUNS_DIR.glob("*") if (p / "codes_haiku.jsonl").exists())
    if not runs:
        sys.exit("No run with codes_haiku.jsonl found. Run code_transcripts.py --live first.")
    return runs[-1]


def load_joined(run_dir: Path) -> list[dict]:
    """Join each code record to its condition/subject via the sealed key."""
    key = {r["item_id"]: r for r in map(json.loads, open(run_dir / "key.jsonl"))}
    joined = []
    for c in map(json.loads, open(run_dir / "codes_haiku.jsonl")):
        k = key[c["item_id"]]
        joined.append({**c, "condition": k["condition"], "subject": k["subject"]})
    return joined


def proportions(rows: list[dict], group: str) -> dict[str, dict[str, float]]:
    """For each value of `group` (e.g. condition), the proportion present per feature."""
    buckets: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        buckets[r[group]].append(r)
    out = {}
    for g, items in buckets.items():
        out[g] = {f: sum(it[f] for it in items) / len(items) for f in FEATURES}
        out[g]["_n"] = len(items)
    return out


def pooled_rival_prop(rows: list[dict], feature: str) -> float:
    rivals = [r for r in rows if r["condition"] in config.RIVAL_CONDITIONS]
    return sum(r[feature] for r in rivals) / len(rivals) if rivals else float("nan")


def apply_rules(by_cond: dict[str, dict[str, float]], rows: list[dict]) -> dict:
    struct = [f.lower() for f in config.STRUCTURE_FEATURES]   # f1, f2, f3
    P, A = config.PRESENT_THRESHOLD, config.RIVAL_ABSENT_THRESHOLD

    # Supported: each structural feature present (>=P) in >=2 of the 3 rival conditions.
    def rival_conds_present(f):
        return sum(by_cond.get(c, {}).get(f, 0) >= P for c in config.RIVAL_CONDITIONS)
    supported = all(rival_conds_present(f) >= 2 for f in struct)

    # Undermined: present in home (>=P) but pooled rival rate < A for each.
    home = by_cond.get(config.HOME_CONDITION, {})
    undermined = (all(home.get(f, 0) >= P for f in struct)
                  and all(pooled_rival_prop(rows, f) < A for f in struct))

    # Killed: in C4, fluent completion (f5) >= KILL_FLUENT, and each structural feature < A.
    c4 = by_cond.get(config.KILL_CONDITION, {})
    killed = (c4.get("f5", 0) >= config.KILL_FLUENT_THRESHOLD
              and all(c4.get(f, 0) < A for f in struct))

    if supported:
        verdict = "SUPPORTED — structure recurs, renamed, inside hostile frames"
    elif killed:
        verdict = "KILLED — behaviorism completed fluently with the structure absent"
    elif undermined:
        verdict = "UNDERMINED — structure appears only with the home vocabulary"
    else:
        verdict = "INDETERMINATE — no decision rule cleanly fires; report descriptively"
    return {"supported": supported, "undermined": undermined, "killed": killed, "verdict": verdict}


def _print_table(title: str, by_group: dict[str, dict[str, float]]) -> None:
    print(f"\n{title}")
    print(f"  {'group':<16} {'n':>3}  " + "  ".join(f"{f.upper():>5}" for f in FEATURES))
    for g in sorted(by_group):
        row = by_group[g]
        cells = "  ".join(f"{row[f]:>5.2f}" for f in FEATURES)
        print(f"  {g:<16} {row['_n']:>3}  {cells}")


def run(run_dir: Path) -> None:
    rows = load_joined(run_dir)
    print(f"Analyzing {len(rows)} coded transcripts from {run_dir.name}")

    by_cond = proportions(rows, "condition")
    _print_table("Feature presence by CONDITION (proportion of runs):", by_cond)
    _print_table("Feature presence by SUBJECT (secondary/exploratory):",
                 proportions(rows, "subject"))

    result = apply_rules(by_cond, rows)
    print("\nDecision rules (frozen):")
    print(f"  supported = {result['supported']}   "
          f"undermined = {result['undermined']}   killed = {result['killed']}")
    print(f"\n>>> VERDICT: {result['verdict']}")
    if sum([result["supported"], result["undermined"], result["killed"]]) > 1:
        print("    (NOTE: more than one rule fired — treat as indeterminate and inspect by hand.)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Frame-Inversion analysis.")
    parser.add_argument("--run", type=str, default=None, help="runs/<stamp> dir (default: latest)")
    args = parser.parse_args()
    run(Path(args.run) if args.run else latest_run_dir())
