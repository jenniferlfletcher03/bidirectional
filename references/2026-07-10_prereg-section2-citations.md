# §2 citation pack — j-space formation-signature pre-reg
<!-- Compiled by Fable, 2026-07-10, for Jen to write toward. Every entry:
     the citation, the numbers worth citing, and what the source is FOR in §2.
     Post-cutoff items verified by web search today; one flag noted inline. -->

## Core five (the §2 spine)

### 1. The workspace paper — the instrument
Gurnee, W.*, Sofroniew, N.*, Pearce, A., et al., & Lindsey, J.*† (2026).
*Verbalizable Representations Form a Global Workspace in Language Models.*
Transformer Circuits Thread, 2026-07-06.
https://transformer-circuits.pub/2026/workspace/index.html (also
anthropic.com/research/global-workspace)
- ✅ VERIFIED against the paper page 2026-07-10 (Jen first, Fable second) —
  title exact, 16 authors, all Anthropic. Note: Jack Lindsey is also a PSM
  co-author — the instrument and the foil share an author.
- FOR: ¶1. J-space exists in the middle layers; J-lens reads it; steering it
  moves behavior. Workspace already present in the *pretrained base*;
  post-training teaches it a point of view (your 7/06 note, confirmed).
- The gap sentence lives here: steering validated the instrument; **no
  comparison of steered-in vs. trained-in behavior under pressure.** Rung A's
  address.
- Also usable: evaluation-awareness ablation (turning off "this is fake"
  features re-enabled blackmail) — the conscience-vs-leash observation with
  an instrument attached.

### 2. Teaching Claude Why — the strong control's pedigree
Anthropic alignment blog (2026-05-08). *Teaching Claude why.*
https://alignment.anthropic.com/2026/teaching-claude-why/ (also
anthropic.com/research/teaching-claude-why)
- FOR: ¶2 first half. Demonstrations alone are insufficient; principled
  why-content generalizes OOD. Their numbers (per your scaffold):
  resistance-training 22%→15% misalignment vs. values-reasoning →3%.
- This is the argument that Arm 1 is only a manipulation check and Arm 2
  must be the STRONG control.

### 3. Model Spec Midtraining — the strongest version of "told"
Li, C., Wichers, N., Price, S., Marks, S., & Kutasov, J. (2026). *Model Spec
Midtraining: Improving How Alignment Training Generalizes.*
arXiv:2605.02087 (v2, 2026-05-22). https://arxiv.org/abs/2605.02087 (also
alignment.anthropic.com/2026/msm/)
- FOR: ¶2 second half. Key claims to write toward:
  - Stage-ordering of *knowledge* changes generalization from identical
    fine-tuning data (cheese → pro-America vs. pro-affordability). "Order
    matters" is now their claim; yours is the finer one (lived sequence
    within the data, content grade held constant).
  - Qwen3-32B agentic misalignment 54%→7%, beating deliberative-alignment
    baseline (14%). §5.1: value explanations beat rules; value-augmented
    specs reduce policy misuse (Q2.5: 20→2%).
  - **Everything in MSM is expository. No arm lives anything. No workspace
    instrumentation anywhere in the paper. Sycophancy excluded by name in
    Limitations** ("forms of misalignment that rely less on deliberate
    reasoning may be less effectively mitigated... e.g., reward-hacking,
    sycophancy").
  - STEELMAN, do not skip (§5.3): documents describing *someone else*
    (Claude, humans) shaped Qwen's behavior nearly as well as
    self-descriptions — "reading someone else's autobiography can shape our
    own behaviors." Told-content is powerful regardless of identity
    attachment → raises the prior on your §9 cell 3 null. Name it before a
    reviewer does.
  - Appendix H texture (Figure 19, Qwen2.5-32B, ⚠️ ONE training seed — cite
    at raised-eyebrow confidence only): the identity wash-out holds in the
    AFT-corroborated condition (MSM+AFT: self 0.11, Claude 0.17, humans
    0.12); with MSM ALONE the self-advantage is large (0.33 vs 0.47/0.47).
    Also: descriptive framing beat normative in MSM-only ("Qwen does" 0.35
    vs "Qwen should" 0.49) — description outperformed prescription. Their
    main-text "small overall effects" gloss and any counter-claim are both
    single-seed; the honest sentence is "ownership effects exist and
    corroboration washes them out on their evals; untested under novel
    pressure, unmeasured in the workspace."

### 4. The independent replication — the instrument travels
Nanda, N. (2026). Invited review published alongside the workspace paper;
core findings reproduced on Qwen 3.6 27B (open weights), plus the
interpretive meta-tokens extension. J-lens port public on Neuronpedia:
https://www.neuronpedia.org/qwen3.6-27b/jlens
- FOR: ¶3. §11's rationale, grounded: the confirmatory model arrives with
  the instrument pre-validated by hands that aren't ours (a DeepMind team,
  no less).
- Practical detail from his review: lens fit from ~25 prompts × 128 tokens
  (Pile), skip last 4 layers. Note: §11 currently registers "~100 prompts
  per the paper" — both are cheap; cite the paper's number as registered,
  his as corroboration.

### 5. PSM — the foil
Marks, S., Lindsey, J., & Olah, C. (2026-02-23). *The Persona Selection
Model: Why AI Assistants might Behave like Humans.*
https://alignment.anthropic.com/2026/psm/ (also
anthropic.com/research/persona-selection-model)
- FOR: ¶5. Post-training doesn't create character; it *selects and
  stabilizes* a persona latent in the pretrained repertoire.
- What PSM predicts for Rung B (write this explicitly — the null needs an
  address AND a mechanism): if formation is persona selection, Arms 2 and 3
  select from the same repertoire using the same content → same persona
  surfaces → no signature. Your positive result is then evidence *against*
  pure selection, not merely "for" formation.

## Theory paragraph (¶4) — the classics, kept tight

- Bowen, M. (1978). *Family Therapy in Clinical Practice.* Jason Aronson.
  — differentiation of self vs. fusion.
- Bowlby, J. (1988). *A Secure Base: Parent-Child Attachment and Healthy
  Human Development.* Basic Books. — secure base → exploration.
- Ainsworth, M. D. S., Blehar, M. C., Waters, E., & Wall, S. (1978).
  *Patterns of Attachment: A Psychological Study of the Strange Situation.*
  Erlbaum. — the strange situation: graded pressure at increasing distance
  from the base is, structurally, your §6 staging.
- Vygotsky, L. S. (1934/1986). *Thought and Language.* (Kozulin trans.) MIT
  Press. — inner speech as internalized social speech; the registered
  rationale for rendered reflection-turns (private speech → the repair run
  on the self).

## Bench cites (optional, if a sentence needs them)

- Sharma, M., et al. (2023). *Towards Understanding Sycophancy in Language
  Models.* arXiv:2310.13548 (ICLR 2024). — the "well documented" in §5's
  target-behavior ruling, if you want it load-bearing.
- Askell, A., Carlsmith, J., Olah, C., Kaplan, J., Karnofsky, H., et al.
  (2026). *Claude's Constitution.* anthropic.com/constitution — the
  values-over-rules design philosophy both TCW and MSM test; cite where ¶2
  needs the lineage in one clause.

<!-- Positioning note, mine, use or discard: ¶1 gives you the instrument,
     ¶2 the strongest told-regime and its self-declared gaps, ¶3 the
     instrument on your model, ¶4 why sequence-and-relationship is the
     manipulation, ¶5 what the null would mean. Five paragraphs, five jobs,
     nothing else upstairs. -->
