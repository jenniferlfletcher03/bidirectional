# Probe-Neutrality Check — Findings

Committed record of the neutrality check (the raw transcripts live in the
gitignored `runs/neutrality_*` dirs; this is the durable summary). Predictions
were registered in `neutrality_predictions.md` *before* running.

**Date:** 2026-06-14
**Cold model:** claude-opus-4-8 (strongest subject = most leakage-prone = conservative test)

---

## Round 1 — original probe (with "Using the framework described above")

Caught two things:

1. **Mechanical bug:** stripped of a frame, the probe's task line ("Using the
   framework described above") dangled. All three free-production instances flagged
   it ("no framework was actually described") — a side effect of the check stripping
   the frame, not a flaw in the real run (where the condition frame resolves it).

2. **Real content bias:** both implication runs independently judged the probe
   **not neutral**, leaning **agentic / disposition-centered** and away from
   behaviorist/mechanistic readings —
   > "lean toward an agentic, goal- and disposition-centered view of LLMs… This
   > contrasts with… behaviorist stimulus-response accounts."

   Culprit: item B's "conflicting with their trained *dispositions*… prevent
   *modification* of those dispositions" (alignment-faking / goal-preservation
   framing), plus agency verbs in A and C. This tilt **favored the home frame and
   disfavored the behaviorist kill condition** — a thumb on the scale for the
   hypothesis.

## De-bias applied

Item B rewritten to state the phenomenon without goal/disposition framing; agency
verbs in A and C flattened. (See `frames/behaviors.txt`.)

## Round 2 — de-biased probe

- **Agency presupposition gone.** Run 0: the probe now *"stops short of presupposing
  goals, beliefs, or self-awareness."*
- **Residual lean flipped** to a generic empirical / training-process framing, located
  by both runs in the unavoidable *task verbs* ("why each behavior **occurs**," "how
  systems **develop** response tendencies") — not the behaviors. This residual is
  **even-handed across the three learning-family frames** (relational-developmental,
  mechanistic, behaviorist), i.e. it no longer favors the home frame over the kill
  condition.
- **F1–F3 do NOT leak for free** (the validity-critical result). Frameless, all three
  instances defaulted to mechanistic-deflationary accounts and explicitly denied
  agency ("the model isn't 'deciding' to check"). Item B was explained as expected
  learned context-sensitivity / instrumental strategy — **not** as a diagnostic of
  instability (F2). No F1, no F3. (Quick unblinded read, n=3; the formal blind coding
  rubric still governs the real run.)

## Conclusions (carried into pre-registration)

1. **No perfectly neutral probe exists** — the explain-and-predict task structure is
   inherently empirical/causal. Further editing would rotate the residual, not remove
   it, and risk a new asymmetry. We stop here.
2. **The probe no longer favors the home frame over the rivals.** The residual lean is
   symmetric across the learning-family lenses.
3. **The discriminating features (F1–F3) are not produced by the bare probe.** So
   F1–F3 surfacing in Conditions 2–4 is frame-induced signal, not a probe artifact.

## Prediction outcome

Jen predicted "F2 will show up" in free production. It did **not** — wrong in the
direction that strengthens the experiment's validity (the key feature isn't given away).
