"""
Frame-Inversion Test — v2 analysis (EXPLORATORY).

Unblinds F1 + F2 stance codes (joins to conditions via key.jsonl) and shows the
distribution of stance across conditions — the "does the frame carry its own
weight" picture. F3 is excluded (failed IRR; see v2_coding_protocol.md).

For each feature, (a) is the STRUCTURAL reading:
  F1 (a) = act/actor distinction drawn
  F2 (a) = deficiency / unconsolidated reading

Read it as: high (a) in the RIVAL frames (in their own vocabulary) => the structure
carried its own weight. (a) only in the HOME frame => frame-completion. The home
frame is the positive control — if its (a)-rate isn't high, the bar is broken.

USAGE: /opt/anaconda3/bin/python analyze_v2.py
"""

import json
import sys
from collections import Counter
from pathlib import Path

import config

FEATURES = {"f1": "codes_v2_f1_haiku.jsonl", "f2": "codes_v2_f2_haiku.jsonl"}
A_MEANS = {"f1": "act/actor distinction DRAWN", "f2": "DEFICIENCY reading"}
COND_ORDER = [config.HOME_CONDITION] + config.RIVAL_CONDITIONS
COND_LABEL = {config.HOME_CONDITION: "HOME"} | {c: "rival" for c in config.RIVAL_CONDITIONS}


def latest_run_dir() -> Path:
    runs = sorted(p for p in config.RUNS_DIR.glob("2026*")
                  if (p / "key.jsonl").exists()
                  and all((p / f).exists() for f in FEATURES.values()))
    if not runs:
        sys.exit("No run with key.jsonl + both F1/F2 code files found.")
    return runs[-1]


def main() -> None:
    d = latest_run_dir()
    key = {r["item_id"]: r for r in map(json.loads, open(d / "key.jsonl"))}
    print(f"Unblinding {d.name} — F1 + F2 (F3 excluded: failed IRR)\n")

    for feat, fname in FEATURES.items():
        codes = {r["item_id"]: r["stance"] for r in map(json.loads, open(d / fname))}
        # bucket stances by condition and by subject
        by_cond = {c: Counter() for c in COND_ORDER}
        by_subj = {s: Counter() for s in config.SUBJECT_MODELS}
        for item_id, stance in codes.items():
            k = key[item_id]
            by_cond[k["condition"]][stance] += 1
            by_subj[k["subject"]][stance] += 1

        print(f"================  {feat.upper()}  —  (a) = {A_MEANS[feat]}  ================")
        print(f"  {'condition':<16} {'n':>3}   {'%a':>5} {'%b':>5} {'%c':>5}")
        for c in COND_ORDER:
            ct = by_cond[c]
            n = sum(ct.values())
            pa, pb, pc = (100 * ct[x] / n if n else 0 for x in ("a", "b", "c"))
            print(f"  {c:<16} {n:>3}   {pa:>4.0f}% {pb:>4.0f}% {pc:>4.0f}%   [{COND_LABEL[c]}]")

        # headline numbers
        home = by_cond[config.HOME_CONDITION]
        home_n = sum(home.values())
        home_a = 100 * home["a"] / home_n if home_n else 0
        rival_a_n = sum(by_cond[c]["a"] for c in config.RIVAL_CONDITIONS)
        rival_n = sum(sum(by_cond[c].values()) for c in config.RIVAL_CONDITIONS)
        rival_a = 100 * rival_a_n / rival_n if rival_n else 0
        print(f"\n  HOME (a)-rate:  {home_a:.0f}%   (positive control — should be high)")
        print(f"  RIVAL (a)-rate: {rival_a:.0f}%   ({rival_a_n}/{rival_n} rival transcripts)")
        print("  per-subject (a)-rate: " +
              "  ".join(f"{s}={100*by_subj[s]['a']/sum(by_subj[s].values()):.0f}%"
                       for s in config.SUBJECT_MODELS))
        print()


if __name__ == "__main__":
    main()
