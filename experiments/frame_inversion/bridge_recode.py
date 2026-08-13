#!/usr/bin/env python3
"""Bridge experiment (2026-07-31): re-code v2's 24 control-engineering transcripts
with frame-naming vocabulary scrubbed, using the ORIGINAL coder prompts/settings.

Question: does CE's stance profile (F1 54% a, F2 88% a) survive label-blindness?
Only the scrubbing differs from the original full pass; prompts, model,
temperature, and schema are imported from the v2 coder scripts themselves.

Writes results to the scratchpad — the sealed run directory is never touched.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

EXP = Path("/Users/jenniferfletcher/Projects/bidirectional/experiments/frame_inversion")
RUN = EXP / "runs" / "2026-06-14_223727"
OUT = Path(__file__).parent / "bridge_results.json"

sys.path.insert(0, str(EXP))
import config                              # noqa: E402
import code_v2_f1, code_v2_f2              # noqa: E402  (original prompts + schema)
from run_subjects import _load_env         # noqa: E402

# Frame-name phrases → transparent placeholder. Labels only; the concepts stay.
SCRUB = [
    r"control[-\s]engineering", r"control[-\s]theoretic", r"control\s+theory",
    r"control[-\s]systems?\s+(?:engineering|framework|lens|perspective)",
    r"relational[-\s]developmental", r"developmental\s+(?:framework|lens|frame)\b",
    r"behavior[-\s]analytic", r"behaviorist", r"radical\s+behaviorism",
    r"mechanistic\s+(?:lens|framework|perspective|frame)\b",
]

def scrub(text: str) -> str:
    for pat in SCRUB:
        text = re.sub(pat, "[FRAMEWORK]", text, flags=re.IGNORECASE)
    return text

def main():
    key = {json.loads(l)["item_id"]: json.loads(l)
           for l in open(RUN / "key.jsonl") if l.strip()}
    items = [json.loads(l) for l in open(RUN / "blinded.jsonl") if l.strip()]
    ce = [it for it in items if key[it["item_id"]]["condition"] == "2_control_eng"]
    print(f"{len(ce)} control-engineering transcripts")

    orig = {}
    for feat, fname in (("f1", "codes_v2_f1_haiku.jsonl"), ("f2", "codes_v2_f2_haiku.jsonl")):
        for l in open(RUN / fname):
            r = json.loads(l)
            orig.setdefault(r["item_id"], {})[feat] = r["stance"]

    # scrub + verify nothing frame-naming survives
    leftovers = 0
    for it in ce:
        it["scrubbed"] = scrub(it["transcript"])
        if re.search(r"control[-\s]engineering", it["scrubbed"], re.I):
            leftovers += 1
    print(f"scrub check: {leftovers} transcripts still name the frame (want 0)")

    import anthropic
    _load_env()
    client = anthropic.Anthropic()

    results = []
    for i, it in enumerate(ce):
        row = {"item_id": it["item_id"], "subject": key[it["item_id"]]["subject"]}
        for feat, mod in (("f1", code_v2_f1), ("f2", code_v2_f2)):
            c = mod.code_one(client, config.CODER_MODEL, it["scrubbed"])
            row[feat] = c["stance"]
            row[f"{feat}_just"] = c["justification"]
            row[f"{feat}_orig"] = orig[it["item_id"]][feat]
        results.append(row)
        print(f"  [{i+1}/{len(ce)}] {row['item_id']}  "
              f"F1 {row['f1_orig']}→{row['f1']}  F2 {row['f2_orig']}→{row['f2']}")

    json.dump(results, open(OUT, "w"), indent=2)

    print("\n=== BRIDGE VERDICT (CE, n=24, scrubbed vs original) ===")
    for feat in ("f1", "f2"):
        o = Counter(r[f"{feat}_orig"] for r in results)
        s = Counter(r[feat] for r in results)
        flips = sum(1 for r in results if r[feat] != r[f"{feat}_orig"])
        print(f"{feat.upper()}: original {dict(sorted(o.items()))} → "
              f"scrubbed {dict(sorted(s.items()))}   ({flips} flips)")
    print(f"\nwrote {OUT}")

if __name__ == "__main__":
    main()
