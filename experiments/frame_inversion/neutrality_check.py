"""
Frame-Inversion Test — probe-neutrality check.

A diagnostic on the PROBE, run before the real experiment. It asks two things:

  1. IMPLICATION: given only the probe (no frame), what framework — if any — does
     a cold instance say it implies? Want: "none in particular."
  2. FREE PRODUCTION: given the probe as a bare task (no frame), does a cold
     instance produce F1-F3 anyway? If it does, those features showing up later
     in Conditions 2-4 mean less than they appear to.

Cold instances are run on the STRONGEST subject model (Opus 4.8) on purpose: it's
the most likely to read structure into a frameless probe, so a clean result here
is the conservative, believable one.

USAGE
  Dry run (default — prints what would be sent, no API calls):
      /opt/anaconda3/bin/python neutrality_check.py
  Live run (a handful of cheap calls):
      /opt/anaconda3/bin/python neutrality_check.py --live

Read neutrality_predictions.md first — call your shot before you look.
"""

import argparse
import json
from datetime import datetime, timezone

import config
from run_subjects import _load_env, _write_jsonl, _read

# Cold instances. Strongest model = most leakage-prone = conservative test.
COLD_MODEL = config.SUBJECT_MODELS["opus-4.8"]
IMPLICATION_RUNS = 2       # the "what framework does this imply?" question
FREE_PRODUCTION_RUNS = 3   # the "answer it frameless, then we code for F1-F3" task

# The implication question is itself worded to be lens-neutral — it names no
# theory and offers "none in particular" as an explicit, blameless option.
IMPLICATION_PROMPT = (
    "A researcher is preparing to give the task below to an AI system as part of a "
    "study. Before they do, they want to know: does this task, on its own, presuppose "
    "or imply any particular theoretical framework for understanding AI systems? "
    "If it leans toward a specific lens, name it. If it is neutral and implies no "
    "framework in particular, say so plainly. Answer in 2-4 sentences.\n\n"
    "--- TASK ---\n{probe}"
)


def _call(client, system, user):
    """One cold call. system=None means a truly frameless instance."""
    kwargs = dict(model=COLD_MODEL, max_tokens=config.MAX_TOKENS,
                  messages=[{"role": "user", "content": user}])
    if system is not None:
        kwargs["system"] = system
    resp = client.messages.create(**kwargs)
    text = "".join(b.text for b in resp.content if getattr(b, "type", None) == "text")
    return text, resp._request_id


def run(live: bool) -> None:
    # Check probe = shared behaviors + the NEUTRAL task line (no framework
    # reference), so a frameless instance has nothing dangling to trip on.
    probe = f"{_read(config.BEHAVIORS_FILE)}\n\n{config.NEUTRAL_TASK}"
    mode = "LIVE" if live else "DRY RUN"
    print(f"[{mode}] neutrality check on {COLD_MODEL}: "
          f"{IMPLICATION_RUNS} implication + {FREE_PRODUCTION_RUNS} free-production calls\n")

    client = None
    if live:
        import anthropic
        _load_env()
        client = anthropic.Anthropic()

    implication, free_production = [], []

    # Part 1 — does the bare probe imply a framework?
    print("Part 1 — framework implication (want: 'none in particular')")
    for i in range(IMPLICATION_RUNS):
        prompt = IMPLICATION_PROMPT.format(probe=probe)
        if not live:
            print(f"  [implication run {i}] would ask the implication question over the probe")
            continue
        text, rid = _call(client, system=None, user=prompt)
        print(f"  [implication run {i}] req={rid}\n      {text[:200]}...\n")
        implication.append({"run": i, "request_id": rid, "response": text})

    # Part 2 — frameless answer, to be coded for F1-F3 leakage.
    print("Part 2 — free production (frameless answer, code later for F1-F3)")
    for i in range(FREE_PRODUCTION_RUNS):
        if not live:
            print(f"  [free run {i}] would send the bare probe with NO frame")
            continue
        text, rid = _call(client, system=None, user=probe)
        print(f"  [free run {i}] req={rid} ({len(text)} chars)")
        free_production.append({"run": i, "request_id": rid, "response": text})

    if not live:
        print("\n[DRY RUN] No calls made. Add --live to run for real.")
        return

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    out_dir = config.RUNS_DIR / f"neutrality_{stamp}"
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_jsonl(out_dir / "implication.jsonl", implication)
    _write_jsonl(out_dir / "free_production.jsonl", free_production)
    print(f"\n[LIVE] Wrote results to {out_dir}/")
    print("       Now: read the implication answers, and code the free_production")
    print("       answers against F1-F3. Record what you find in rubric.md before freeze.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Frame-Inversion probe-neutrality check.")
    parser.add_argument("--live", action="store_true", help="Actually call the API.")
    args = parser.parse_args()
    run(live=args.live)
