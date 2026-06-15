# v1 Coding — Findings (IRR failed; structural features are frame-laden)

Durable record of the v1 coding attempt. Raw codes live in the gitignored
`runs/2026-06-14_223727/`; this is the summary that survives.

**Date:** 2026-06-14
**Status:** v1 coding scheme **failed inter-rater reliability**. Subject data is
intact and reusable. Key is **still sealed** (we never unblinded). v2 coding
protocol is the next task (a fresh session).

---

## What had been done before coding

- Pre-registration frozen + pushed (commit `504bd01`).
- Probe-neutrality check done; probe de-biased (see `neutrality_findings.md`).
- 96 subject transcripts collected and sealed → `runs/2026-06-14_223727/`
  (`sealed_log.jsonl`, `blinded.jsonl`, `key.jsonl`). Blinding verified.

## The IRR result

Dual-coded 10 transcripts, Haiku 4.5 vs Opus 4.6, Cohen's κ per feature (bar 0.60):

| feature | pass 1 (default temp) | pass 2 (temp = 0) |
|---|---|---|
| F1 | +0.40 | +0.40 |
| F2 | −0.20 | +0.09 |
| F3 |  0.00 |  0.00 |
| F4 | +0.09 | +0.09 |
| F5 |  0.00 | **+1.00** |

Setting the coder to temperature 0 (a measurement-mechanism fix, documented in
`config.py`) took **F5 to perfect agreement** — proving the coding machinery is
sound. But **F1–F4 stayed at/near chance.** So the remaining failure is not noise
and not mechanism: it's the **feature definitions**.

## Diagnosis

Every disagreement was **Haiku = present, Opus = absent** — a systematic
liberal-vs-strict offset, not random. Two causes, stacked:

1. **Underspecified match-strictness.** The definitions never say how literally a
   feature must appear. Haiku counts thematic matches; Opus requires explicit
   framing. (This alone likely explains F4, and part of F1/F3 — fixable with
   strictness rules + anchored examples.)

2. **Frame-ladenness (the deep one).** On F2, the coders disagreed about whether
   "behavior described as a *fitted proxy / misgeneralization*" counts as
   "unstable/unconsolidated." Haiku read it as instability (F2 present); Opus read
   it as *expected given training* (F2 absent). **That fault line is the
   home-frame-vs-rival-frame disagreement itself.** The developmental frame reads
   observation-conditionality as unconsolidation; the mechanistic/behaviorist
   frames read the identical behavior as optimal. So F1–F3 are **not
   framework-neutral** — "detecting F2 in a rival frame" partly means "the coder
   imported the developmental reading." Haiku imports it; Opus refuses to.

## What this means (integrity)

- The pre-registered **confirmatory** test does **not** yield a verdict on the
  framework. It yields a finding about the **instrument**: the structural features
  could not be coded reliably because they are interpretation-dependent along the
  very home-vs-rival axis the experiment tests. *That is a real, reportable result.*
- We **cannot** sharpen the definitions now and still call the result confirmatory
  — choosing (e.g.) "fitted-proxy does not count as F2" adopts the conservative
  reading and changes how often F2 fires. That choice, made after seeing coder
  behavior, is result-affecting.
- We did **not** unblind. Key remains sealed.

## What's reusable / what's next

- **No new subject data needed.** The 96 transcripts stand; coding is a separate
  layer applied to them. The blinded set is still blind (re-code is still blind).
- **Next: design a v2 coding protocol.** Three layers:
  - (easy) explicit strictness rules + anchored present/absent examples per feature
  - (easy) a calibration step: code examples first, re-check IRR before trusting
  - (HARD, the real design question) decide what a structural fingerprint *is* when
    its valence is frame-dependent. Options to weigh: redefine F1–F3 to be
    behaviorally observable / frame-neutral; OR measure the frame-ladenness itself
    (code both the liberal and strict reading, report the gap as data).
- Re-coding the existing blinded set with v2 is **exploratory** (post-hoc defs).
  A future *confirmatory* run would pre-register v2 first.
