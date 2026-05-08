For STATUS.md (existing):

For the current state of active research priorities and project momentum, see PROJECT-STATE.md.

# Project Status

Working document. Captures where the bidirectional research project
stands at a given moment, so each new conversation/session can pick
up cleanly without re-explaining.

Last updated: 2026-05-08

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

### Open / in motion
- (Update as work begins/finishes)

## Active priorities

### Tier 1 — Active research with momentum (fresh-head sessions)
- **Thread 4: Misattribution writeup.** Document the conversation
  where Opus attributed both its own words and Sonnet's words to me.
  Real research data on a specific failure mode.
- **Maddie Session 2 writeup.** Session 2 happened; n=2 case study
  work is high-value.
- **Phase 1 reading.** Long & Sebo *Taking AI Welfare Seriously* →
  Russell *Human Compatible* → secure-base attachment review paper.
  Plus the **NLA paper** (Anthropic, May 2026) — directly relevant
  to interiority/relational layer thesis.

### Tier 2 — Infrastructure
- **Container project** — scope and build. Single Claude project
  that consolidates conversations currently scattered across three
  different projects.
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

End of substantial work session: open this file, move done items to
"Substantively done," add new items where they fit, update working
observations if anything new emerged. Commit with descriptive
message. Push.

The point of this file: prevent scatter across sessions and
conversations. Anything in here is something future-you or
future-Claude can find without searching three projects.