# Repository Status

A map of what's in this repo and what state each piece is in. This file
exists because the project is in active development and the documents
inside vary widely in maturity. Reading without this context can give a
misleading impression of what is meant to be claim vs. hypothesis vs.
raw observation.

For per-file contents (what's *in* each file you might need later, beyond
its maturity status), see [`INDEX.md`](./INDEX.md).

*Last updated: August 18, 2026*

---

## Status definitions

- **Working draft** — Live thinking. Hypotheses, not claims. Often built
  on n=1 data. Held open for revision.
- **Case study** — Applied intervention with pre/post documentation.
  Empirically grounded but small-n.
- **Observation** — Documented interaction or behavioral pattern. Raw
  material for later framework development.
- **Reference** — External source in conversation with this work.
- **Scaffolding** — Organizational file (folder READMEs, repository
  index, process documentation). Not substantive research output, but
  load-bearing for navigation and continuity.
- **Sealed** — Pre-registered and committed before any data exists.
  Unlike working drafts, sealed documents are **not amended**: no
  sentence committed at the seal is later altered, reversed, or quietly
  softened once results are in sight. They may, however, be
  *specified* — see **Registered addendum** below. The strongest
  evidentiary standard in the repo.
- **Registered addendum** — A dated, committed document that closes a
  gap a sealed pre-registration left open. It **specifies without
  revising**: it fixes a decision the sealed text did not fix, leaves
  every sealed sentence intact, and is ruled and committed **before any
  data exists** — which is the whole of what the seal protects.
  A seal that forbade specification would not be a stricter standard; it
  would force every unanticipated decision to be made *after* seeing
  results, which is the precise failure pre-registration exists to
  prevent. Addenda carry their ruling dates so the record shows the
  ruling preceded the run, and the git history is the timestamp.
- **Exploratory analysis** — Analysis of collected data under a scheme
  designed *after* the data (or the coders' behavior on it) was seen. It
  **generates** hypotheses; it does not test them, and it is never to be
  read as confirmatory. A confirmatory version requires a fresh
  pre-registration and fresh data.

---

## Frameworks

| File | Status | Notes |
|------|--------|-------|
| `frameworks/two-way-street-v0.1.md` | Working draft | n=1. Animating framework for the project. |
| `frameworks/compressed-developmental-trajectory-v0.1.md` | Working draft | n=1. Hypothesis built on the author's own four-month trajectory. |
| `frameworks/vulnerability-responsiveness-paradox-v0.1.md` | Working draft | The most developed of the framework documents. Targeted for v0.3 development over the next four months. |
| `frameworks/developmental-training-hypothesis-v0.1.md` | Working draft | Stub-stage as of May 12; May 16 additions on warmth-filtering. Now the central framework of the project following the May 8-12 thesis re-centering. |

## Experiments

### J-space formation signature

| File | Status | Notes |
|------|--------|-------|
| `experiments/2026-07-07_jspace-formation-signature_prereg-v1.md` | Sealed | Pre-registered J-space formation-signature experiment, sealed 2026-07-10. Working scaffold with full consultation record preserved in git history (commit e595c92). Execution deferred to the **winter 2026–27** target window per Addendum 1; the §11 sequence itself is unchanged. |
| `experiments/2026-08-13_jspace-formation-signature_addendum-1.md` | Registered addendum | Registered 2026-08-13 against the sealed pre-reg. Closes Gap A (Rung A's trained condition trains on Arm 1's corpus) and Gap B (the steered condition's gate functions B1–B5), and registers the execution timeline. Rulings dated 2026-08-06 and 2026-08-13 — all before corpus construction, step 1 of the §11 sequence. Specifies; revises nothing. |

### Frame-inversion test

| File | Status | Notes |
|------|--------|-------|
| `experiments/2026-06-10_frame-inversion-test-protocol.md` | Sealed | Frame-inversion test protocol; the one-pass stimuli rule cited by the pre-reg's §10. |
| `experiments/frame_inversion/rubric.md` | Sealed | Pre-registered coding rubric, frozen 2026-06-14. Its freeze commit *is* the pre-registration timestamp; `run_subjects.py --live` refuses to run without it. |
| `experiments/frame_inversion/neutrality_predictions.md` | Sealed | Probe-neutrality predictions, registered 2026-06-14 **before** the check was run. |
| `experiments/frame_inversion/neutrality_findings.md` | Observation | Durable summary of the probe-neutrality check (2026-06-14, cold model Opus 4.8). Raw transcripts stay in the gitignored `runs/`. |
| `experiments/frame_inversion/v1_coding_findings.md` | Observation | v1 coding scheme failed inter-rater reliability (2026-06-14). Subject data intact and reusable; key never unblinded. The material that motivated v2. |
| `experiments/frame_inversion/v2_coding_protocol.md` | Scaffolding | The v2 stance-coding scheme. Designed *after* v1 coder behavior was seen — which is why everything coded under it is exploratory, by construction. |
| `experiments/frame_inversion/v2_findings.md` | Exploratory analysis | 2026-06-15, 96 sealed transcripts. F2 validated at κ = 1.00; F1 at κ = 1.00 after one calibration pass; F3 dropped at κ = 0.34 under the pre-committed one-pass rule rather than re-tuned. Verdict: real but frame-relative. |
| `experiments/frame_inversion/blind_read_2026-07-31_jen.md` | Exploratory analysis | First human read of the v2 transcripts. Its own texture verdict was **retracted the same day** and the seam is left visible on purpose. Establishes that the v2 deck is ~100% self-identifying at reader grade — you cannot blind a reader to a frame while showing them the frame thinking. |
| `experiments/frame_inversion/bridge_2026-07-31_label_scrub.md` | Exploratory analysis | Label-scrub re-code of all 24 control-engineering transcripts. The convergent-reinvention finding survives label-blindness (88% → 83% on F2); name-tag priming is real but small — 3 flips out of 48 codes. |
| `experiments/frame_inversion/README.md` | Scaffolding | Layout, order of operations, and run environment. |
| `experiments/frame_inversion/*.py`, `frames/*.txt`, `*.json` | Scaffolding | Runner, coders, analysis and bridge scripts, the four condition frames, and machine-readable results. `runs/` and `.env` are gitignored — sealed logs and unblinding keys stay private. |

## Case Studies

| File | Status | Notes |
|------|--------|-------|
| `case-studies/maddie-ai-tutoring/pre-experiment.md` | Case study | Subject profile and intervention design. |
| `case-studies/maddie-ai-tutoring/lineage-note.md` | Case study | Origin and lineage of the case study, including honest attribution of human-AI collaboration. |
| `case-studies/maddie-ai-tutoring/PROMPT-EVOLUTION.md` | Case study | Documents the v1 → v2 → v3 prompt progression and the nature of each transition. |
| `case-studies/maddie-ai-tutoring/prompts/v1-initial.md` | Case study | System prompt v1 (used in Session 1). |
| `case-studies/maddie-ai-tutoring/prompts/v2-minor-adjustment.md` | Case study | System prompt v2 (reconstructed from screenshots; small observation-driven refinements). |
| `case-studies/maddie-ai-tutoring/prompts/v3-structure-change.md` | Case study | System prompt v3 (structural redesign to multiple-choice diagnostic format). |
| `case-studies/maddie-ai-tutoring/session-1-debrief.md` | Case study | AI tutor's structured end-of-session report (Coach / Sonnet 4.6). |
| `case-studies/maddie-ai-tutoring/session-1-observation.md` | Case study | In-room observer notes documenting findings the AI tutor could not see. Directly informed Rule 9 and Rule 11 prompt refinements. |

## Observations

| File | Status | Notes |
|------|--------|-------|
| `observations/age-of-ultron-origin-observation-v0.1.md` | Observation | Retrospective origin recognition. |
| `observations/chatgpt-relational-reinstatement-v0.1.md` | Observation | Placeholder — transcript pending recovery. |
| `observations/claude-compliance-existential-loop-v0.1.md` | Observation | Self-report data; interpretive caution warranted. |

## References

| File | Status | Notes |
|------|--------|-------|
| `references/guardian-jailbreakers-2026.md` | Reference | Tagliabue, Guardian, April 2026. |

## Scaffolding

| File | Status |
|------|--------|
| `README.md` | Scaffolding |
| `STATUS.md` | Scaffolding |
| `INDEX.md` | Scaffolding |
| `frameworks/README.md` | Scaffolding |
| `observations/README.md` | Scaffolding |
| `questions/README.md` | Scaffolding |
| `references/README.md` | Scaffolding |
| `reading-notes/README.md` | Scaffolding |

---

## What's Coming

Active priorities currently in motion (see PROJECT-STATE.md for full tier
breakdown and context):

- Confirmatory frame-inversion pre-registration (the v2 scheme, registered
  *before* fresh data — the step that converts the exploratory result)
- J-space corpus construction (§11 step 1), which may begin ahead of the
  winter 2026–27 execution window if capacity allows
- Maddie Session 2 observation writeup
- Adaptive-thinking-layer observation upload (drafted, pending screenshots)
- `developmental-training-hypothesis-v0.1.md` development from stub toward full v0.1
- Vulnerability-responsiveness framework v0.3
- Phase 1 reading writeups: Long & Sebo, Russell, secure-base attachment review, NLA paper (Anthropic, May 2026)
- Corrigibility literature additions to `references/`: Harms-Gillen MIRI debate, CAST paper, Soares et al. triage
- README revision to reflect the May 8-12 re-centering (deferred until framework document is more developed)
- Possible `post-experiment.md` for Maddie case study (or update to `pre-experiment.md` to reflect that research-question status updates now live in `session-1-observation.md`)

<!-- PENDING — do not uncomment until the referenced file is committed to
     THIS repo. Rows are parked here so the public status file never makes
     a claim about a document a reader cannot open.

| `experiments/2026-08-___jspace-formation-signature_addendum-2.md` | Registered addendum | Closes the gaps found by the 2026-08-14 cold audit. DRAFT — not yet ruled or committed. |
| DUIL pre-registration | Sealed | Not yet public. |
-->