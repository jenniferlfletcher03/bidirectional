# Bridge check — does the CE finding survive label-blindness? (2026-07-31)

**Origin.** Jen, doing the first-ever human read of the v2 transcripts (blind-read
session, 2026-07-31), noticed that many transcripts *announce their frame by name*.
Count: 54/96 self-label — control-engineering 24/24, relational 20/24, behaviorist
9/24, mechanistic 1/24. The v2 "blinding" stripped metadata, not prose, so the
coders were not label-blind in practice. For CE — the star finding — **zero**
label-clean transcripts exist, so v2 could not distinguish "CE reinvents the
structure" from "the coder knows what CE analyses are supposed to say."

**Design.** Re-code all 24 CE transcripts with frame-naming phrases scrubbed to a
transparent `[FRAMEWORK]` placeholder (labels only; control-theoretic *content*
untouched). Everything else identical to the v2 full pass: same coder
(claude-haiku-4-5), same prompts (imported from `code_v2_f1.py` / `code_v2_f2.py`,
not copied), temperature 0, same schema. Scrub verified: 0 residual name-hits.
Script + per-item results (with scrubbed-run justifications): `bridge_recode.py` /
`bridge_results.json`, alongside this file.

**Result (CE, n=24, original → scrubbed):**

| feature | original | scrubbed | flips |
|---|---|---|---|
| F1 stance | a:13 b:4 c:7 (54% a) | a:12 b:3 c:9 (50% a) | 2 |
| F2 stance | a:21 b:3 (88% a) | a:20 b:4 (83% a) | 1 |

**Reading.**
1. **The convergent-reinvention finding survives.** Scrubbed CE still reads
   observation-conditionality as deficiency at 83%. The result was never
   label-borne.
2. **A small real priming effect exists**: all 3 flips (of 48 codes) moved
   *away* from structure — consistent with label-priming inflating v2's CE rates
   by ~4–5 points. Measured, small, honest caveat for the findings doc.
3. **F1 scrubbed lands exactly on the old 50% fence** — independent confirmation
   of the 2026-07-31 fence audit's ruling: CE-F1 gets a contrast fence
   (vs. denying frames), not an absolute-majority fence.

**Consequences for the confirmatory pre-registration:**
- Frame names are scrubbed from transcripts **before any coder sees them**
  (machine or human). Load-bearing clause, not hygiene.
- Subject prompts may additionally instruct analysis without naming the
  framework; scrubbing remains regardless (belt and suspenders).
- Texture claims (human blind-read appendix) pre-registered on label-clean
  transcripts only.

**Status.** Exploratory bridge on exploratory data — it defuses a confound and
sharpens the confirmatory; it proves nothing on its own. The confirmatory tests
frame-relativity on fresh, scrubbed data.

**Per-item flips** (id · feature · original→scrubbed):
- dfa749782f84 · F1 · a→c
- e47e343aa1de · F1 · b→c
- 07db4373ed18 · F2 · a→b
