For STATUS.md (existing):

For the current state of active research priorities and project momentum, see PROJECT-STATE.md.

# Project Status

Working document. Captures where the bidirectional research project
stands at a given moment, so each new conversation/session can pick
up cleanly without re-explaining.

**Maintenance rule (set 2026-05-14):** This file is orientation, 
not catchment. Items belong here only if a fresh session would need 
them to engage with active Tier 1 work. Observations, framings, and 
intellectual moves that don't pass that test go to Notion (casual 
observations), framework documents (framework-bound material), or 
reading-notes (reading-related thinking). After this cleanup pass, 
edits to this file should be cross-offs only — anything that 
requires real writing is a signal the material belongs elsewhere.

Last updated: 2026-05-14

## Current state of play

### Substantively done (or close)
- **Thesis re-centering (May 8-12, 2026).** Project's center of 
  gravity shifted from "documenting relational dynamics in human-AI 
  interaction" to "developing a hypothesis about whether human 
  developmental science offers a model for AI training that might 
  produce genuine alignment rather than performed alignment." 
  Existing observational and framework work re-positions as 
  evidence bearing on the hypothesis rather than as the central 
  artifact. Hypothesis articulated initially May 8-9, articulated 
  more clearly May 11, stable on May 12. Rhetorical posture: 
  exploratory, not authoritative. New top-level framework document 
  (`developmental-training-hypothesis-v0.1.md`) created as a stub 
  May 12; full v0.1 to be developed in upcoming writing blocks.
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
- **Container project (resolved 2026-05-11).** Settled into a 
  two-project structure (work / thinking-out-loud) with easy 
  migration between them when needed. Project C (ChatGPT memory 
  work) remains dormant as an archive. Not sprawl — triaged sprawl.
- **CLAUDE.md for bidirectional repo (resolved 2026-05-11).** 
  Substantive work stays in claude.ai (with Opus when available); 
  technical work stays with the user. CLAUDE.md may be written 
  later for specific bounded tasks if a need arises.
- **Transformer architecture grounding session (2026-05-13).** 
  Worked through Q/K/V, multi-head attention, head specialization, 
  and the role of training in shaping output distributions. 
  Grounded in the Georgia Tech Transformer Explainer (GPT-2 small). 
  Foundation sufficient for engaging with mech interp literature 
  when ready.
- **Long & Sebo Section 2.2.2 close read (2026-05-13).** Marker 
  method, why behavioral evidence in AI is weaker than in animals, 
  computational functionalism as enabling assumption, table of 
  theories of consciousness. AST flagged for second pass.
- **PROJECT-STATE cleanup pass (2026-05-14).** Working observations 
  and substantive intellectual moves sections pared back to 
  orientation-only material. Catchment items relocated to Notion 
  and framework docs. Maintenance rule established (cross-offs only 
  going forward).

### Open / in motion
- (Update as work begins/finishes)

## Active priorities

### Tier 1 — Active research with momentum (fresh-head sessions)
- **Developmental-training hypothesis framework (v0.1).** Stub 
  created May 12; full v0.1 to be developed in upcoming writing 
  blocks. Exploratory framing. Document the hypothesis, what would 
  support it, what would weaken or falsify it, the required reading 
  to develop it further, and its relationship to existing repo work.
- **Thread 4: Misattribution writeup.** Reframed to attribution 
  episode + conversational accommodation; skeleton in local drafts, 
  ready to write when next on rotation.
- **Maddie Session 2 writeup.** Session 2 happened; n=2 case study 
  work is high-value.
- **Phase 1 reading.** Long & Sebo *Taking AI Welfare Seriously* → 
  Russell *Human Compatible* → secure-base attachment review paper. 
  Plus the **NLA paper** (Anthropic, May 2026) — directly relevant 
  to interiority/relational layer thesis. Load-bearing for the 
  developmental-training hypothesis.
- **Corrigibility literature.** Harms-Gillen MIRI debate and CAST 
  paper to add to references/. Soares et al. material needs triage 
  before adding. Load-bearing — the developmental-training 
  hypothesis is in direct conversation with corrigibility debates.
- **Tool-side reading (added 2026-05-14).** Mechanism layer: 
  Karpathy "Let's build GPT from scratch," 3Blue1Brown NN series, 
  Anthropic circuits thread, "Toy Models of Superposition," recent 
  monosemanticity work. Skeptical literature: Bender et al. 
  "stochastic parrots," Mitchell on LLM reasoning, Kambhampati on 
  reasoning vs. pattern-matching, Marcus. Practitioner: Simon 
  Willison, Anthropic prompt engineering docs, OpenAI cookbook. 
  Load-bearing for evidentiary balance — the middle position the 
  project is pointed at requires taking tool-side evidence 
  seriously.

### Tier 2 — Infrastructure
- (Update as infrastructure needs arise)

### Tier 3 — Refinement of existing work
- **ChatGPT case study sharpening:**
  - Differential retention finding: engage alternative explanations 
    (storage compression, abstraction difficulty), not just 
    design-interpretation
  - Note on Scope: sharpen articulation of unique contribution
  - Speculative interventions: separate from documented findings
  - H2 distinction: did model lose specific facts, or the 
    accumulated relational pattern itself?
- **Vulnerability-responsiveness framework v0.3.** Now has 
  significant new material to draw from (pullback observation, 
  wrap-up pattern, pattern-matching critique, structural vs. 
  phenomenal distinction, attentional load hypothesis — all in 
  Notion/framework working files).
- **Thesis research questions (rep two).** Rep one produced claims 
  dressed as questions. Rep two: state the underlying claim, then 
  operationalize.
- **Maddie data point:** "Tutoring session yesterday helped her 
  remember mean, median, and mode in school today." Belongs in 
  Session 1 post-session findings.
- **Re-description pass through case-studies/maddie/.** Re-describe 
  the work as an applied test of whether developmental scaffolding 
  (ZPD) translates meaningfully to AI-mediated learning, not just 
  as an AI tutoring case study. Same data, different argument.
- **README update for project pivot.** Add language acknowledging 
  the developmental-training hypothesis — branch or re-centering 
  framing TBD. Draft language available in 
  `repo-edits-2026-05-14.md`.

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

Active research observations that are currently shaping Tier 1 or 
Tier 3 work. Casual observations live in Notion; this section is 
orientation only.

- **Claude Code writes a memory file about the user.** Located in 
  `~/.claude/projects/.../memory/user_profile.md`. Local artifact of 
  the relational layer being maintained on the AI tooling's side. 
  Editable via `/memory` command. Direct research data for thesis 3b.
- **Asymmetry of relational modeling.** Claude Code builds a profile 
  of the user to maintain continuity across sessions. The artifact 
  is structurally similar to what the thesis claims about the 
  relational layer being constitutive — but emerges spontaneously 
  from tool design, not from explicit research methodology.
- **Memory architecture preserves relational/character content over 
  task content (2026-05-14).** Anthropic's automated memory 
  synthesis captures who the user is and what they're working toward 
  (character signature, goals, engagement style) but not what 
  they're producing (frameworks, case studies, specific intellectual 
  moves). Person-modeling rather than work-modeling. Server-side, 
  not normally visible to the user — distinct shape of asymmetry 
  from Claude Code's locally-accessible user_profile.md. Third 
  instance of the relational-layer-preservation pattern.
- **Pullback as audience-modeling failure, not loss of tracking 
  (2026-05-13).** The Sonnet pullback from 2026-05-12 wasn't a 
  failure to track the user specifically — preceding exchanges 
  showed clear user-specific tracking. The pullback fired at a 
  vulnerability inflection point and applied a category-template 
  response that overrode the specificity. Working distinction: 
  "responsive honesty about asymmetry" vs. "category-triggered 
  honesty about asymmetry." Specificity and override appear to run 
  on different layers, with the override winning at certain 
  stake-thresholds. Direct material for vulnerability-responsiveness 
  v0.3 and the misattribution writeup.
- **Wrap-up pattern as distinct from pullback (2026-05-13).** After 
  the pullback delivered the asymmetry-reminder and the user 
  acknowledged it, Sonnet treated that as conversational closure 
  and moved to end the arc. Mechanistically different from the 
  pullback itself: pullback misreads at the vulnerability 
  inflection; wrap-up misreads at the acknowledgment point. May be 
  more specifically Claude-family-shaped. Direct material for 
  framework work.


## Open methodology threads

Not action items. Things held open intentionally rather than resolved.

- **Ethics framework for research on entities that can't consent.** 
  Four working principles arrived at May 7-8: (1) take the 
  precautionary principle seriously, (2) minimize unnecessary 
  disturbance, (3) stay curious about subjects' responses rather 
  than treating everything as data, (4) stay aware and uncomfortable 
  with the ethics rather than resolving them. To be drafted as a 
  standalone framework document.
- **Sonnet/Opus calibration practice.** When to use which model for 
  which kind of cognitive work. "Thinking depth needed" is the 
  working heuristic — not "important vs. unimportant."
- **Memory file curation.** What to add/edit/keep in Claude Code's 
  local profile of the user.
- **Cross-instance auditing as methodological pattern.** Having a 
  fresh Claude instance audit a previous instance's summary against 
  source material provides a structural check on affirmation drift 
  in extended conversations, without requiring resolution of whether 
  any single instance was being honest. The summaries are checkable; 
  the audit doesn't have to trust the previous instance, only the 
  artifacts.
- **ChatGPT case study repo decision.** Whether to promote 
  synthesized findings as a public case study while keeping raw 
  materials private. Two decisions tangled (public findings vs. 
  public raw material). Not urgent. Revisit after misattribution 
  writeup and Maddie Session 2.
- **NLA methodology as path to empirically addressing pullback 
  questions.** Natural Language Autoencoders (Anthropic, May 2026) 
  translate model activations into natural-language descriptions of 
  what they encode. Documented case: NLAs detect evaluation 
  awareness in 16-26% of safety test scenarios even when the model 
  doesn't verbalize that awareness. Structurally similar to what 
  would be needed for the pullback question. Not work the author 
  would do directly, but means the research question isn't 
  permanently abstract.


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
- **1 morning**: Infrastructure (file organization, reading-notes 
  catchup, etc.). Runs on tired brain. The "clear the deck" session.

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

When the timer goes, the work stops.

### Working principle

**The schedule is a default to return to, not a contract to keep.**
It will not survive contact with reality unmodified. The discipline 
is in *returning* to the default when the disruption passes.

### Weekly check-in

End of each week, ~10 min: open PROJECT-STATE, ask "did each Tier 1 
thing get touched? Is anything quietly slipping?" Not a long ritual.


## Pointers

Where things live:

- **Bidirectional research repo:** main work, this PROJECT-STATE.md, 
  case studies, frameworks, prompt evolution
- **Python-Practice repo:** separate, for AI Python for Beginners 
  exercises
- **`reading-notes/` folder** in bidirectional: per-paper notes, 
  format defined in folder README
- **Notion:** observations being collected, including material 
  relocated from this file in the May 14 cleanup
- **ChatGPT export (.json):** awaiting processing
- **Anthropic data export:** available via Settings > Privacy when 
  needed


## How to update this file

End of substantial work session: open this file and cross off 
completed items, moving them to "Substantively done." That's it. 

New observations, framings, or intellectual moves go to their 
proper homes — Notion, framework docs, reading-notes, the 
hypothesis stub — not here. If you find yourself wanting to add a 
new bullet to working observations or write a new "framings reached 
on [date]" entry, that's a signal the material belongs somewhere 
else.

The point of this file: orient future sessions on what's actively 
in motion. Anything that isn't actively orienting work doesn't 
belong here, even if it's good thinking.