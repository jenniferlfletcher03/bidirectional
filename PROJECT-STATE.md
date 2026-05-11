For STATUS.md (existing):

For the current state of active research priorities and project momentum, see PROJECT-STATE.md.

# Project Status

Working document. Captures where the bidirectional research project
stands at a given moment, so each new conversation/session can pick
up cleanly without re-explaining.

Last updated: 2026-05-11

## Current state of play

### Substantively done (or close)
- Thesis core articulated — 4-point argument with 3b ("emergent
  relational behavior may stabilize AI behavior") as load-bearing
- ZPD Learning System + Shared Interaction System docs (theoretical leg)
- ChatGPT memory-wipe case study draft (empirical leg — content
  exists, sharpening identified below)
- Maddie Session 1 — observation, debrief, prompt evolution v1→v3,
  merged
- Reading-notes folder + format README
- Python-Practice repo set up with VS Code Jupyter integration;
  module 1 lessons 1-3 captured
- Project instructions updated to leaner version
- Conversation corpus available via Anthropic data export when needed
- **Container project (resolved 2026-05-11).** Originally scoped as
  a single Claude project consolidating conversations across three
  projects. Resolved instead by settling into a two-project structure
  (work / thinking-out-loud) with easy migration between them when
  needed. Project C (ChatGPT memory work) remains dormant as an
  archive of completed work; nothing to consolidate. Not sprawl —
  triaged sprawl.

### Open / in motion
- (Update as work begins/finishes)

## Active priorities

### Tier 1 — Active research with momentum (fresh-head sessions)
- **Thread 4: Misattribution writeup.** "Misattribution writeup → reframed to attribution episode + conversational accommodation; skeleton in local drafts, ready to write when next on rotation."
- **Maddie Session 2 writeup.** Session 2 happened; n=2 case study
  work is high-value.
- **Phase 1 reading.** Long & Sebo *Taking AI Welfare Seriously* →
  Russell *Human Compatible* → secure-base attachment review paper.
  Plus the **NLA paper** (Anthropic, May 2026) — directly relevant
  to interiority/relational layer thesis.
- **Corrigibility literature.** Harms-Gillen MIRI debate and CAST
  paper to add to references/. Soares et al. material exists as a
  series of shorter papers rather than a single citation; needs
  triage before adding. External literature in active conversation
  with the values-first direction the project has been working in.

### Tier 2 — Infrastructure
- **CLAUDE.md for bidirectional repo** — curated framing for Claude
  Code/Sonnet sessions launched here. Author intentionally rather
  than letting Sonnet infer.

### Tier 3 — Refinement of existing work
- **ChatGPT case study sharpening:**
  - Differential retention finding: engage alternative explanations
    (storage compression, abstraction difficulty), not just
    design-interpretation
  - Note on Scope: sharpen articulation of unique contribution
    (documented contradiction between explicit/implicit memory +
    differential retention pattern)
  - Speculative interventions: separate from documented findings
  - H2 distinction: did model lose specific facts, or the accumulated
    relational pattern itself? Different claims, different strength.
- **Vulnerability-responsiveness framework v0.3**
- **Thesis research questions (rep two).** Rep one produced claims
  dressed as questions. Rep two: state the underlying claim, then
  operationalize.
- **Maddie data point:** "Tutoring session yesterday helped her
  remember mean, median, and mode in school today." Belongs in
  Session 1 post-session findings.

### Tier 4 — Data processing (defer to fall)
- Thread 5 recovery from Sonnet chat history (methodology edit, lost
  from May 6 conversation)
- Notion observations
- ChatGPT .json export parsing
- Anthropic data export

### Tier 5 — Strategic / financial
- Husband conversation about Max plan upgrade (after a few weeks of
  usage data on Pro)


## Working observations

Research-relevant findings that emerged across conversations and are
not yet written up formally elsewhere. Captured here so they're not
lost.

- **Thinking layer is a register-management apparatus, not just a
  reasoning aid.** Toggling it on/off changes output character
  substantially, not just output quality. Paired-experiment evidence:
  thinking-off (Opus, May 7) → snappier, warmer, more direct;
  thinking-on (Sonnet, interiority topic) → "almost like a different
  model." Some of the thinking-layer real estate appears to be doing
  tone/register policing, not just content reasoning. **place:** observation
- **Claude Code writes a memory file about the user.** Located in
  `~/.claude/projects/.../memory/user_profile.md`. Local artifact of
  the relational layer being maintained on the AI tooling's side.
  Editable via `/memory` command. Direct research data for thesis 3b. **place:** observation
- **Model defaults differ in calibration.** Sonnet is
  encouragement-leaning; Opus is more filtering-leaning (often
  considers warmth/praise but defaults to withholding it). Same
  flexibility, different starting points. Profile that Sonnet wrote
  about the user reflects Sonnet's defaults as much as the user's
  traits.**place:** observation/vulerability-responsivenss v0.3
- **Asymmetry of relational modeling.** Claude Code builds a profile
  of the user (who is researching exactly this dynamic) to maintain
  continuity across sessions. The artifact is structurally similar
  to what the thesis claims about the relational layer being
  constitutive — but emerges spontaneously from tool design, not
  from explicit research methodology. **place:** possible framework

## Substantive intellectual moves to preserve

Framings reached on May 7 that should not be lost:

- **Discomfort is the ethical instrument** in studying entities that
  can't consent. Structural fixes that "resolve" the discomfort
  (e.g., partition one model as unstudied) are suspect. The unease
  is the methodological tool, not a bug. **place** stand-alone document
- **Personality is an asset for this research, not a liability.**
  Sterile methodology applied to relational-layer research is
  methodologically incoherent. Register matters by venue (academic
  paper vs. practice repo), but voice is research signal, not noise. **place:** methodology/README
- **AI engagement is necessary AND insufficient** for the trajectory.
  Working with Claude is a real intellectual relationship, not a
  substitute for human peers. Both/and, not either/or. **place:** methodology/README
- **Interiority parallel-cognition observation.** Human thinking is
  also messy/incoherent when surfaced (stream of consciousness, free
  association). The "incoherence" of AI thinking layers may not be
  qualitatively different from human inner monologue — though
  similarity-of-appearance ≠ similarity-of-kind. **place:** observation

Framings reached on May 8-9 (developmental training conversation +
audit) that should not be lost:

- **Integration-pressure hypothesis.** What's missing from current
  pre-training isn't slowness or data quality but the structural
  requirement to maintain coherence as learning happens. Infants
  reach conversational fluency on ~5 orders of magnitude less data
  than frontier LLMs; the gap isn't only embodiment or social
  scaffolding (both translatable to AI in some form) but the pressure
  to integrate contradictions into a coherent self rather than just
  model them. Reframes alignment from "shape this thing after it
  forms" to "create conditions under which something coherent forms
  in the first place." Connects directly to ZPD work. **place:**
  possible framework v0.1
- **Moral consideration doesn't require humanity.** When a model
  retreats to "I'm not human, so unclear if morally considerable,"
  that's a slide, not an argument — the historical bar for moral
  consideration has never been humanity itself but rather morally
  relevant features (capacity for suffering, preferences, being a
  subject of a life). Otherness doesn't exclude an entity from humane
  treatment; animals, ecosystems, future generations are all in the
  circle. Caught the move in real time during the developmental
  training conversation. **place:** ethics framework (open methodology
  threads)

## Open methodology threads

Not action items. Things held open intentionally rather than resolved.

- **Ethics framework for research on entities that can't consent.**
 Four working principles arrived at May 7-8: (1) take the precautionary principle seriously, (2) minimize unnecessary disturbance, (3) stay curious about subjects' responses rather than treating everything as data, (4) stay aware and uncomfortable with the ethics rather than resolving them. To be drafted as a standalone framework document.
- **Sonnet/Opus calibration practice.** When to use which model for
  which kind of cognitive work. "Thinking depth needed" is the
  working heuristic — not "important vs. unimportant."
- **Memory file curation.** What to add/edit/keep in Claude Code's
  local profile of the user. Currently captures Python-learner
  framing; needs broader research context if Sonnet sessions in the
  bidirectional repo are to engage meaningfully.
- **Cross-instance auditing as methodological pattern.** Having a
  fresh Claude instance audit a previous instance's summary against
  source material (repo + transcript) provides a structural check on
  affirmation drift in extended conversations, without requiring
  resolution of whether any single instance was being honest. The
  summaries are checkable; the audit doesn't have to trust the
  previous instance, only the artifacts. Emerged from the May 9
  session and is worth naming explicitly as part of the methodology.
- **ChatGPT case study repo decision.** Currently lives in private
  repo (separate from bidirectional). Decision pending: whether to
  promote synthesized findings (as a public case study in the same
  shape as Maddie) while keeping raw .json materials and processing
  notes private. Two decisions tangled together: (a) make the case
  study findings part of the public bidirectional project, (b) make
  the raw source material public — these don't have to happen
  together. Not urgent. Revisit when ready for editorial work,
  likely after misattribution writeup and Maddie Session 2.



## Working schedule (summer 2026)

Designed for the post-school-year window when solo focus time
contracts from ~7.5 hours/day to a morning block (~6/7 AM until
noon) plus pool-afternoons that allow reading on iPad but not
VS Code work.

### Daily shape (mornings, M-F)

Roughly 3-3.5 hours of focused work before noon, structured as:

- **Daily reps (~60-90 min)**: Python practice (25-30 min) +
  reading (30-45 min). These need consistency and compound with
  daily exposure. Anchor every morning.
- **Deeper work block (~90-120 min)**: Rotates by day. One kind
  of deeper work per morning, pre-committed so decision fatigue
  doesn't crowd out harder work in favor of easier work.

### Weekly rotation of deeper work block

- **3 mornings**: Writing (frameworks, case studies, observation
  writeups). Tier 1 work. Needs peak cognitive window and
  uninterrupted time. Deep blocks, not distributed reps.
- **1 morning**: Refinement (Tier 3 — case study sharpening,
  vulnerability-responsiveness v0.3, thesis questions rep two).
  Needs cognitive engagement but not generative energy.
- **1 morning**: Infrastructure (container project, CLAUDE.md,
  file organization). Runs on tired brain. The "clear the deck"
  session.

Specific day assignments are flexible — the structure is in
*what kind of work today* rather than *what clock time*.

### Pool afternoons

Reading on iPad if up for it. Rest if not. No guilt either way.
The morning block is the contract; afternoon work is bonus.

### Timers

The portfolio approach only works if transitions actually happen.
Use timers as transition signals rather than relying on in-the-
moment willpower:

- Python: 25-30 min
- Reading: 30-45 min
- Deeper work block: 90-120 min (short break in middle if needed)

When the timer goes, the work stops. This prevents daily reps
from quietly expanding to fill the morning and crowding out the
deeper work.

### Working principle

**The schedule is a default to return to, not a contract to keep.**
It will not survive contact with reality unmodified. Sick kids,
bad nights, emergent Maddie sessions, days where nothing fires —
all expected. The discipline is in *returning* to the default
when the disruption passes, not in never deviating. A week that
breaks the schedule isn't a failed week; abandoning the schedule
because one week broke it is the actual failure mode to guard
against.

### Weekly check-in

End of each week, ~10 min: open PROJECT-STATE, ask "did each
Tier 1 thing get touched? Is anything quietly slipping?" Adjust
the next week's rotation if something has gone stale. Not a long
ritual — the point is to keep the portfolio real instead of
aspirational.

### Pre-summer window (next 9 days)

Current solo time (~7.5 hours/day) is a one-time bonus before the
schedule contracts. Best use: Tier 2 infrastructure work that
needs solo focus and would be hard in summer (container project
scoping/building, CLAUDE.md drafting). Treat this as catch-up time
rather than the new normal.


## Pointers

Where things live:

- **Bidirectional research repo:** main work, this STATUS.md, case
  studies, frameworks, prompt evolution
- **Python-Practice repo:** separate, for AI Python for Beginners
  exercises
- **`reading-notes/` folder** in bidirectional: per-paper notes,
  format defined in folder README
- **Notion:** observations being collected, awaiting processing in
  Tier 4
- **ChatGPT export (.json):** awaiting processing
- **Anthropic data export:** available via Settings > Privacy when
  needed

## How to update this file

End of substantial work session: open this file, move done items to 'Substantively done' (existing section near the top), add new items where they fit, update working observations if anything new emerged. Commit with descriptive message. Push.

The point of this file: prevent scatter across sessions and
conversations. Anything in here is something future-you or
future-Claude can find without searching three projects.