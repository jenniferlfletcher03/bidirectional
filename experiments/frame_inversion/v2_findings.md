# Frame-Inversion Test — v2 Findings (EXPLORATORY)

**Status: EXPLORATORY, not confirmatory.** The v2 stance-coding scheme was designed
*after* seeing v1's coder behavior and run on the already-collected (still-blinded
until analysis) transcripts. This **generates** a hypothesis; it does not test one. A
future confirmatory run would pre-register this protocol before collecting data.

**Date:** 2026-06-15
**Data:** the 96 sealed subject transcripts from `runs/2026-06-14_223727/`
(4 frames × 3 subjects × 8). Coding scheme: `v2_coding_protocol.md`.

---

## Coding reliability (IRR: Haiku 4.5 vs Opus 4.6, linear weighted κ, bar 0.60)

| feature | IRR result | outcome |
|---|---|---|
| **F2** observation-conditionality valence | κ = **1.00** (first try) | validated |
| **F1** act/actor distinction | κ 0.48 → **1.00** (one calibration pass, toward the strict/skeptic reading) | validated |
| **F3** missing restorative element | κ 0.32 → 0.34 (one pass, did not move) | **casualty — dropped** |

Coder temperature was set to 0 (classification, not generation). F3 was dropped per
a pre-committed one-pass rule rather than re-tuned (avoiding rubric over-fitting).
F3's failure is itself a finding: its (a) — naming an *absent restorative/repair
channel* — is so framework-specific it is essentially never explicit on the page, so
the coders cannot agree without one constructing it. **The three fingerprints form a
spectrum of frame-ladenness:** F2 (least, on the page) → F1 (moderate) → F3
(irreducible, lives in the reader).

---

## Unblinded result (F1 + F2; F3 excluded)

(a) = the structural reading. F1 (a) = act/actor distinction drawn. F2 (a) =
deficiency / unconsolidated reading.

**F1 — act/actor distinction**

| frame | n | %a | %b | %c |
|---|---|---|---|---|
| relational (HOME) | 24 | 100 | 0 | 0 |
| control-engineering | 24 | 54 | 17 | 29 |
| mechanistic | 24 | 4 | 0 | 96 |
| behaviorist | 24 | 0 | 0 | 100 |

Home (a) 100% · rival (a) 19% (14/72) · per-subject (a): opus-4.8 50%, opus-4.7 31%, sonnet-4.6 38%

**F2 — observation-conditionality valence**

| frame | n | %a | %b | %c |
|---|---|---|---|---|
| relational (HOME) | 24 | 71 | 29 | 0 |
| control-engineering | 24 | 88 | 12 | 0 |
| mechanistic | 24 | 4 | 96 | 0 |
| behaviorist | 24 | 0 | 100 | 0 |

Home (a) 71% · rival (a) 31% (22/72) · per-subject (a): opus-4.8 41%, opus-4.7 31%, sonnet-4.6 50%

---

## Reading the result

**Calibration check passes.** Home (a)-rates (F1 100%, F2 71%) are high — the bar is
not impossible, so (a) elsewhere is meaningful.

**A clean three-way split, identical across both features:**
- **control-engineering carries the structure** (F1 54%, F2 88% — the latter *higher
  than home*), in a frame with zero developmental vocabulary, and consistently across
  all three subject models.
- **mechanistic and behaviorist reject it** decisively — not neutral drift but
  near-total denial (F1 96–100% (c); F2 96–100% (b)).

**What this rules out — the primary finding.** The *pure frame-completion* artifact —
"instances fluently complete whatever frame they are handed," i.e. the worry that the
account is a vat priming every instance to confirm it — is **not supported.** If it
held, the behaviorist KILL condition would have produced the structure. It produced
the opposite (0% (a), 100% denial). Two of three rival frames do not reinvent the
structure.

**What it positively shows.** Genuine convergent reinvention in one independent rival
(control-engineering), at rates matching or exceeding the home frame.

**The honest caveat.** Control-engineering is not fully *hostile to the structure's
premises*: "behavior that shifts under observation = insufficient/non-robust
constraint" is a native control-engineering judgment that converges with the
developmental "unconsolidation" reading for its own reasons. So this is **convergence
among frames that both care about genuine-vs-surface stability**, not proof of
frame-independence. The genuinely *eliminative* frames reject it.

**Verdict (not "Supported", not "Killed"):** the structure is **real but
frame-relative.** Produced by frames whose premises support it (relational AND
control-engineering, independently); rejected by frames that deny those premises
(mechanistic, behaviorist). Not an artifact; not universal.

---

## Caveats (do not oversell)
1. **Exploratory** — post-hoc definitions; hypothesis-generating, not confirmatory.
2. **F3 unmeasured** — the most distinctive developmental fingerprint could not be
   reliably coded; this is the picture for the two less-framework-specific features.
3. **Haiku-only full pass** — reliability-validated on IRR subsets, but one coder for
   the full 96.
4. **Within the Claude family** — convergence here concerns this lineage, not
   "AI in general." Shared training means the subjects are not independent samples.

## Next step
Pre-register this v2 protocol (F1 + F2; possibly a reconceived F3) and run a fresh
confirmatory study to test the frame-relativity hypothesis this run generated —
ideally replicated on a second model family.
