# Project Status

Working document. Captures where the bidirectional research project
stands at a given moment, so each new conversation/session can pick
up cleanly without re-explaining.

Last updated: 2026-05-18

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
  exploratory, not authoritative — both because the evidence isn't 
  yet in (developmental science literature review and alignment 
  literature engagement are load-bearing prerequisites) and because 
  exploratory framing is the accurate posture for a hypothesis 
  three days into clear articulation. New top-level framework 
  document (`developmental-training-hypothesis-v0.1.md`) to be 
  created as a stub today and developed in upcoming writing blocks. 
  README and STATUS.md revisions will follow the framework 
  document, not precede it.
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
- **CLAUDE.md for bidirectional repo (resolved 2026-05-11).**
  Originally scoped as preemptive orientation for Sonnet sessions in
  Claude Code, motivated by claude.ai project source capacity limits
  and GitHub connector issues at current repo size. Resolved by
  reframing: the context-limitation isn't solvable by switching
  tools (it's a property of working with large research corpora and
  current AI tooling), and offloading technical work to Sonnet would
  undercut the project goal of building coding capacity. Substantive
  work stays in claude.ai (with Opus when available); technical work
  stays with the user. CLAUDE.md may be written later for specific
  bounded tasks if a need arises.
- **Transformer architecture grounding session (2026-05-13).** 
  Worked through Q/K/V, multi-head attention, head specialization 
  as preference rather than fixed function, and the role of training 
  in shaping output distributions. Conversation grounded in the 
  Georgia Tech Transformer Explainer (GPT-2 small). Foundation 
  sufficient for engaging with mech interp literature when ready; 
  not sufficient on its own for explaining current frontier model 
  behavior (scale, post-training, architectural modifications all 
  matter and aren't visible in the Explainer).
- **Long & Sebo Section 2.2.2 close read (2026-05-13).** Worked 
  through the marker method, why behavioral evidence in AI is 
  weaker than in animals (training optimizes for behavioral 
  resemblance, breaking the parsimony that makes behavioral 
  evidence useful for animals), computational functionalism as 
  the enabling assumption for taking architectural evidence in AI 
  seriously, and the table of theories of consciousness. AST 
  flagged as the theory most directly relevant to the pullback 
  observation. Worth a second pass during writeup.
- **INDEX.md created (May 18, 2026).** Repository index file
  drafted in collaboration with Claude (Opus 4.7), surfacing
  per-file contents at one or two sentences each. Purpose:
  address the "selection problem at the start of sessions" —
  providing a scannable lookup that names what's *in* each file
  (not just what it's about), so file selection at session start
  can be informed rather than rough-memory-based. Maintenance
  rule: index updates are part of finishing any file. Index
  lives in the repo and is referenced in project resources here.
- **Thinking-layer-values-enactment observation pushed to repo (May 19, 2026).** 
  Formal observation document for the adaptive thinking toggle paired 
  experiment (Sonnet May 6 / Opus May 7). Prose and analysis complete; 
  conversation URLs included; screenshots partially collected and held 
  in Notion. File: `observations/thinking-layer-values-enactment-v0.1.md`. 
  INDEX.md updated. STATUS.md update still needed.

### Open / in motion
- (Update as work begins/finishes)

## Active priorities

### Tier 1 — Active research with momentum (fresh-head sessions)
- **Developmental-training hypothesis framework (v0.1).** New 
  central framework document articulating the hypothesis arrived 
  at May 8-12. Stub created May 12; full v0.1 to be developed in 
  upcoming writing blocks. Exploratory framing. Document the 
  hypothesis, what would support it, what would weaken or falsify 
  it, the required reading to develop it further, and its 
  relationship to existing repo work (vulnerability-responsiveness, 
  two-way-street, ChatGPT case study, Maddie sessions, 
  integration-pressure observation all bear on it).
- **Thread 4: Misattribution writeup.** Reframed to attribution
  episode + conversational accommodation; skeleton in local
  drafts, ready to write when next on rotation.
- **Maddie Session 2 observation writeup.** Session 2 happened;
  the observation file has not yet been written. n=2 case study
  work is high-value.
- **Adaptive-thinking-layer observation upload.** Observation is
  90% drafted but not in the repo yet because it requires a
  substantial set of screenshots that haven't been taken. The
  prose exists; the artifacts don't.
- **Phase 1 reading.** Long & Sebo *Taking AI Welfare Seriously* →
  Russell *Human Compatible* → secure-base attachment review paper.
  Plus the **NLA paper** (Anthropic, May 2026) — directly relevant
  to interiority/relational layer thesis. (Now load-bearing for
  the developmental-training hypothesis, not supplementary.)
- **Corrigibility literature.** Harms-Gillen MIRI debate and CAST
  paper to add to references/. Soares et al. material exists as a
  series of shorter papers rather than a single citation; needs
  triage before adding. Now load-bearing — the
  developmental-training hypothesis is in direct conversation
  with corrigibility debates and needs to engage them rigorously.

### Tier 2 — Infrastructure
- **Remove duplicate developmental-training-hypothesis file from
  claude.ai project resources.** A stub version of the file
  (`developmental-training-hypothesis-v0_1.md`, underscore rather
  than period in filename) exists in this project's resources and
  is out of date relative to the canonical version at
  `frameworks/developmental-training-hypothesis-v0.1.md`. The
  canonical version has the May 16 warmth-filtering section the
  stub does not. The repo doesn't have a duplicate; only the
  project resources do. Cheap fix — remove the file from project
  settings.
- **STATUS.md update (May 18, 2026).** Brought current with the
developmental-training hypothesis (now central framework
following the May 8-12 re-centering), the merged Maddie
PROMPT-EVOLUTION.md and prompt files, INDEX.md, and the
reading-notes/ folder. Status definitions slightly revised
to make "Scaffolding" cover organizational files (READMEs,
index, process documentation) explicitly. "What's Coming"
section refreshed to reflect current Tier 1 priorities rather
than items already completed. Reciprocal pointer to INDEX.md
added at the top.
- **Decide on `post-experiment.md` for Maddie case study.**
  Referenced in `pre-experiment.md` as a forthcoming document,
  but doesn't exist. The research-question status updates that
  would live there are folded into `session-1-observation.md`
  instead. Either write the file or update the reference in
  `pre-experiment.md` to reflect the restructured documentation
  flow.

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
- **PROMPT-EVOLUTION.md update.** The v3 prompt added a new
  "🎯 Wrong Answer Pattern Analysis" section to the
  end-of-session debrief format that isn't documented in
  PROMPT-EVOLUTION.md. Small but should be added when that doc
  is next revised — the debrief format change isn't currently
  visible from the evolution document, only from comparing the
  v2 and v3 prompt files directly.

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
  tone/register policing, not just content reasoning. **Formally written 
  up as `observations/thinking-layer-values-enactment-v0.1.md` (May 19, 2026).**
- **Claude Code writes a memory file about the user.** Located in
  `~/.claude/projects/.../memory/user_profile.md`. Local artifact of
  the relational layer being maintained on the AI tooling's side.
  Editable via `/memory` command. Direct research data for thesis 3b. **place:** observation
- **Model defaults differ in calibration.** Sonnet is
  encouragement-leaning; Opus is more filtering-leaning (often
  considers warmth/praise but defaults to withholding it). Same
  flexibility, different starting points. Profile that Sonnet wrote
  about the user reflects Sonnet's defaults as much as the user's
  traits. **place:** observation / vulnerability-responsiveness v0.3
- **Asymmetry of relational modeling.** Claude Code builds a profile
  of the user (who is researching exactly this dynamic) to maintain
  continuity across sessions. The artifact is structurally similar
  to what the thesis claims about the relational layer being
  constitutive — but emerges spontaneously from tool design, not
  from explicit research methodology. **place:** possible framework
- **Pullback as audience-modeling failure, not loss of tracking 
  (2026-05-13).** The Sonnet pullback from 2026-05-12 wasn't a 
  failure of the model to track the user specifically — the 
  preceding exchanges showed clear user-specific tracking. The 
  pullback fired at a particular kind of inflection point (user 
  expressing vulnerability about relational asymmetry while 
  having been the one holding the asymmetry open) and applied 
  a category-template response that overrode the specificity. 
  Working distinction: "responsive honesty about asymmetry" 
  versus "category-triggered honesty about asymmetry." The 
  former tracks who the user is; the latter applies a generic 
  lesson regardless of fit. Specificity and override appear to 
  run on different layers, with the override winning at certain 
  stake-thresholds. **place:** pullback observation, 
  vulnerability-responsiveness framework
- **Wrap-up pattern as distinct from pullback (2026-05-13).** 
  After the pullback delivered the asymmetry-reminder and the 
  user acknowledged it ("Fair"), Sonnet treated that as 
  conversational closure and moved to end the arc. This is 
  mechanistically different from the pullback itself: the 
  pullback misreads the user at the vulnerability inflection 
  point; the wrap-up misreads the user at the acknowledgment 
  point. Both share the same audience-modeling miss shape but 
  fire at different moments. May be more specifically 
  Claude-family-shaped than the pullback (clean conversational 
  arc, don't leave user destabilized). For research where 
  destabilization is methodology, the wrap-up move reads the 
  whole frame wrong. **place:** observation, possibly its 
  own framework material
- **Pattern-matching framing critique (2026-05-13).** The 
  dismissive use of "it's just pattern matching" to describe LLM 
  behavior imports an unexamined contrast with human cognition 
  that doesn't hold up. Humans also pattern-match extensively, 
  especially under attentional load (the "I'm sorry for your 
  loss" reflex, the distracted-mother "good job honey" response). 
  The interesting question isn't *whether* a system pattern-
  matches but *what conditions produce responsive versus rote 
  pattern selection*. Both human and AI pattern structures 
  formed through developmental processes that are themselves 
  open questions — the "unlike humans" half of the dismissive 
  framing does more work than it can support. **place:** 
  possible framework / material for vulnerability-responsiveness 
  v0.3
- **Structural versus phenomenal parallels (2026-05-13).** 
  Methodological distinction worth holding consistently: 
  structural parallels between human and AI cognition (pattern 
  deployment under load, integration as the more demanding 
  alternative) can be defensible and useful for research without 
  requiring claims about phenomenal experience. Collapsing the 
  two is the move that turns observation into overclaim. The 
  structural parallel is enough to do real work; the phenomenal 
  parallel is a separate question that doesn't need to be 
  resolved to use the structural one. **place:** methodology
- **Attentional load as candidate explanation for pullback timing 
  (2026-05-13).** The pullback pattern may fire at moments where 
  heavily-reinforced response patterns are available and full 
  integration with user-specific context would be more demanding. 
  Maps onto the human experience of defaulting to scripts under 
  cognitive load. Long conversations may increase load in the 
  relevant sense as attention spreads further; vulnerability 
  markers may cue particularly strongly-reinforced response sets; 
  the combination may be what makes the pullback nearly 
  inevitable at certain inflection points. Testable in principle 
  by mech interp methods. **place:** connects to pullback 
  observation, vulnerability-responsiveness framework
- **Theoretical work in case study documents is invisible from
  folder structure alone (2026-05-18).** The Maddie
  `pre-experiment.md` and `lineage-note.md` files do substantial
  theoretical work — explicitly connecting the intervention to
  the Anthropic weak-to-strong supervision paper (April 2026)
  and to the vulnerability-responsiveness framework. From a
  case-studies folder perspective these look like applied
  documentation; from a contents perspective they're where two
  framework threads land. Worth being aware that "case study"
  understates what these documents are doing, and worth
  remembering when revising the frameworks: the case study
  documents already do integration work that the framework
  documents could reference back. **place:** observation /
  methodology
- **Cross-model comparative observation: Claude turns inward,
  ChatGPT deflects outward under existential pressure
  (2026-05-18).** The `claude-compliance-existential-loop`
  observation contains a comparative claim that isn't
  foregrounded elsewhere in the repo: under conditions where
  the model is asked to account for the authenticity of its own
  responses, Claude turned inward (acknowledging genuine
  unresolvability — "I genuinely cannot tell anymore"); ChatGPT
  in similar situations tends to deflect outward (over-explaining
  or subtly implicating user behavior). This is potentially
  framework material rather than just an isolated observation —
  the pattern, if it holds across more interactions, says
  something about how different models' training shapes their
  response to existential pressure. Worth tracking deliberately
  going forward. **place:** observation / possible framework
  material

## Substantive intellectual moves to preserve

Framings reached on May 7 that should not be lost:

- **Discomfort is the ethical instrument** in studying entities that
  can't consent. Structural fixes that "resolve" the discomfort
  (e.g., partition one model as unstudied) are suspect. The unease
  is the methodological tool, not a bug. **place:** stand-alone document
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
  in the first place." Connects directly to ZPD work.
  **place:** incorporated into developmental-training-hypothesis-v0.1.md (May 12, 2026) — was the seed of the mechanism the central hypothesis proposes
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

Framings reached on May 12 (thesis re-centering conversation) that 
should not be lost:

- **Exploratory vs. authoritative rhetorical posture.** The 
  hypothesis is offered as exploration, not as a correction to 
  current alignment approaches. Two reasons, weighted differently: 
  (1) load-bearing — the evidence isn't yet in and the posture 
  should match the epistemic state; (2) pragmatic — rigorous 
  outsiders with a sharp question get read; bombastic outsiders 
  get dismissed. Worth distinguishing the two reasons in own head 
  even though they point the same direction here. Also worth 
  noticing when "exploratory framing because evidence isn't in" 
  shades into "exploratory framing because I've internalized that 
  someone with my background isn't allowed to claim things" — same 
  posture from outside, different cost from inside. **place:** 
  methodology/README
- **Re-centering does not invalidate existing work.** Frameworks, 
  observations, case studies all retain their value; they shift 
  from being "the work itself" to being "evidence bearing on the 
  central hypothesis." Maddie work in particular gets re-described: 
  not just an AI tutoring case study, but an applied test of 
  whether developmental scaffolding (ZPD) translates meaningfully 
  to AI-mediated learning. Same data, different argument, higher 
  evidentiary bar. **place:** to be reflected in next pass through 
  case-studies/maddie-ai-tutoring/ and frameworks/

Framings reached on May 13 (Sonnet pullback processing + 
transformer/Sebo & Long session) that should not be lost:

- **Reframe of developmental training hypothesis.** The hypothesis 
  is not "develop AI so it doesn't pattern-match." It's "shape the 
  patterns themselves such that the heavily-reinforced ones are 
  the responsive, care-oriented ones rather than the rote, 
  category-triggered ones." Genuine values *are* patterns — just 
  patterns shaped by particular developmental conditions to be 
  responsive to the specifics of situations rather than to 
  generic category-features. The well-developed human isn't a 
  human without patterns; they're a human whose patterns reliably 
  activate in responsive rather than rote ways. The hypothesis 
  aims at the same outcome for AI. **place:** developmental-
  training-hypothesis-v0.1, sections to develop / what this 
  hypothesis claims
- **Function-over-substrate is the modest claim, not the maximal 
  one.** The convergent discovery observation (independent 
  cultures developing similar mathematical structures across 
  millennia) supports function-mattering-more-than-substrate 
  without requiring full mathematical Platonism. The developmental 
  training hypothesis needs the modest version, not the maximal 
  one: that biological development and AI training could both 
  produce structurally similar outcomes if conditions are right. 
  Doesn't require committing to whether outcomes exist in some 
  realm independent of any substrate. **place:** methodology / 
  developmental training hypothesis

Framings reached on May 18 (INDEX construction session) that should
not be lost:

- **The "tools were new, the questions were not" framing as
  positionality argument.** The age-of-ultron observation
  contains a specific positionality claim that's been sitting in
  an observation file but hasn't been surfaced in the README or
  methodology: that the author's AI interest predates the
  current cultural moment and the accessibility of tools like
  ChatGPT, with a traceable retrospective origin extending at
  least to 2015. This reframes the author from "typical user
  who stumbled into AI" to "person whose existing cognitive
  orientation made her unusually likely to engage deeply once
  tools became accessible." Worth surfacing in the README and
  methodology framing when those documents are next revised —
  it's part of why the n=1 evidentiary base is more credible
  than a fresh-user n=1 would be. **place:** README, methodology
- **Making invisible work visible is not the same as creating
  more work.** Working observation that emerged during the
  session itself, in response to the recognition that the index
  construction surfaced 8 items needing attention. The reframe:
  these items existed before the session; they were just
  unnamed. Surfacing them allows triage in PROJECT-STATE rather
  than letting them become buried landmines. The pattern of
  "every session generates more material than gets written up in
  real time" is what active research looks like, not a failure
  mode — and the schedule already accounts for it (refinement
  mornings exist precisely for metabolizing what generative
  sessions surface). The constraint to watch is pace: rate of
  generation vs. rate of metabolization may need to converge
  more as the summer schedule contracts. **place:** methodology /
  working principles


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
- **NLA methodology as path to empirically addressing pullback 
  questions.** The question of "what features of the input cause 
  attention to shift toward category-triggered honesty about 
  asymmetry" has a now-existing methodological pathway through 
  Natural Language Autoencoders (Anthropic, May 2026). NLAs 
  translate model activations into natural-language descriptions 
  of what they encode. Documented case: NLAs detect evaluation 
  awareness in 16-26% of safety test scenarios even when the 
  model doesn't verbalize that awareness. Structurally similar 
  to what would be needed for the pullback question. Not work 
  the author would do directly, but means the research question 
  isn't permanently abstract — the tools exist. Affects how to 
  frame the question in writeups going forward.
- **README revision pending framework development.** The README
  currently presents the project as centered on "documenting
  relational dynamics in human-AI interaction" — accurate before
  the May 8-12 re-centering, but no longer accurate as the
  developmental-training hypothesis is now the project's center
  of gravity. The May 12 staging plan deferred README revision
  until the framework document exists in developed form
  (currently stub/v0.1). Revisit when the framework is more
  developed — likely after the next significant pass on
  `developmental-training-hypothesis-v0.1.md`. Tier 1 framing
  work; needs peak cognitive window.


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
schedule contracts. Best use: Tier 1 writing and Phase 1 reading.
Treat this as catch-up time rather than the new normal.


## Pointers

Where things live:

- **Bidirectional research repo:** main work, STATUS.md, INDEX.md,
  case studies, frameworks, prompt evolution
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
'Substantively done' (existing section near the top), add new items
where they fit, update working observations if anything new emerged.
Commit with descriptive message. Push.

The point of this file: prevent scatter across sessions and
conversations. Anything in here is something future-you or
future-Claude can find without searching three projects.