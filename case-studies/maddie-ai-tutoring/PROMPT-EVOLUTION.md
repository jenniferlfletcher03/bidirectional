# Prompt Evolution

This document serves to demonstrate the formation of the three versions of the prompt as they stand now in the prompts folder connected to this case study.

The prompt `v1-initial.md` is the first iteration of this prompt, discussed in more depth in the `lineage-note.md` file.

Prompt `v2-minor-adjustment.md` is a reconstruction of the v2 prompt that was discussed with Claude Sonnet 4.6 in the original conversation where the initial prompt was conceived. The original v2 prompt was overwritten in the conversation and not saved by the observer, necessitating a reconstruction via screenshot of the original conversation. The minor adjustment in the v2 prompt came from a discussion between the observer and Claude about two things that were noted from physical observations of Maddie that Claude could not make but the observer could.

- Maddie locked in the moment the model suggested a mental image of the problem they were working through. For a more detailed description of this moment, please see `session-1-observation.md`.

- The observer corroborated an observation that the model made in its session debrief: that Maddie did not like her correct reasoning mirrored back to her, and got frustrated enough to advocate for herself to the model about it.

These observations from the observer resulted in two small changes to the prompt as documented in `v2-source.png`: that Maddie should be given a mental image when she got stuck, and that she should be given short praise when supplying a correct answer and not required to explain her reasoning. These changes were both small, observation-driven refinements.

After this moment the observer continued the conversation with Claude, noting that Maddie jumped right into voice chat and this was surprising to her. While the observer was thinking externally with Claude about why Maddie likely didn't want to type her responses, she had the idea that the questions could be reformatted to more accurately reflect the SOL environment by providing the questions with multiple choice answers, to which then, if Maddie needed to, she could use voice chat to walk through her reasoning. Sonnet agreed that this was a good idea and laid out how to change the prompt to reflect more of a diagnostic than an open response. This exchange can be seen in `v3-source-1.png`, `v3-source-2.png`,  `v3-source-3.png`, and `v3-source-4.png`. The four core changes that Sonnet proposed were that each problem needed:

- A question
- Four answer choices where the wrong answers are designed to catch predictable errors
- Instructions that the model should ask her to defend her choice out loud
- A protocol for what to do depending on which answer she picked

Sonnet then took a few minutes to redesign the prompt, noting the big structural shift in question format and diagnostic criteria for each answer, the new response protocol based on Maddie's desire to be affirmed in her correct response, and a change in the debrief that now shows the wrong answer patterns that Maddie would display within session.

## The arc

The progression of these prompts shows how collaboration between the observer and AI (Claude Sonnet 4.6) created a genuine artifact that neither could have created on their own. The observer brought the lived experience of being in the room with Maddie during the session, while the model brought its understanding of diagnostic criteria and test question design. The two transitions in this progression are different kinds of changes. v1 → v2 was a set of small refinements within the existing structure, driven by the observer's in-room observations of Maddie. v2 → v3 was a structural redesign. The format idea (multiple choice with voice reasoning, modeled on the SOL Maddie will soon take) came from the observer, and Sonnet reframed that idea into a full diagnostic instrument with engineered distractors and a wrong-answer protocol.
