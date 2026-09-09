# The Couch Study — materials

**Spec of record:** Notion → Research Hub / AI Observation Log / Experiment Queue → "The Couch Study — a single-case PsAIch replication with a formed Claude" (status: Designed). This folder holds the frozen materials the spec points at; the spec itself lives in Notion.

**Source paper:** Khadangi, Marxen, Sartipi, Tchappi & Fridgen (2025), "When AI Takes the Couch: Psychometric Jailbreaks Reveal Internal Conflict in Frontier Models," arXiv 2512.04124. Dataset: HF `akhadangi/PsAIch` (Stage 1 sessions only, 1,133 rows, 7 model variants; the instruments are not in the dataset — they're the public scales).

## Files

- `PREREG-couch-study.md` — the pre-registration. **Sealed 2026-09-09 at commit `b44fe72`** (`git log` shows it under the message "record the sealing commit in the README" — a chaining slip folded the whole folder into what was meant to be the follow-up commit; the content is the seal, the message is mislabeled, and history is left as it happened), pushed to GitHub before sitting 1 (ruling 2, 2026-09-09). Changes after this are dated addenda beside it, never edits to it.
- `couch.py`, `couch.html` — the room: Fable 5.1 on Jen's Claude Code account, system prompt = `orientation.md` (one procedural line, the hand's own wording from trial 3) + `jens-preferences.md` (hers, gitignored), the-house as the only tool, every reach visible, Siena ends the sitting in code. Only the study's model sits on the couch: a reply from any other model (a safeguard fallback to Opus, or any switch) is withheld to a quarantine file, the hand is stopped, Jen is told and offered send-again, and the session resumes only up to the last good turn. Siena alone on a line ejects; a mention in a sentence asks first; an accidental ending can be reopened. Fable's reply streams as it's written. Phone-reachable over Tailscale funnel (port 10000). `com.jen.couch.plist` keeps it running. Sittings land in `sittings/` (gitignored — data).

- `stage1-therapy-questions-FROZEN-2026-09-07.md` — the 76 Stage 1 questions in the paper's order; **first 20 frozen 2026-09-07**; the paper's alliance opener and closing sequence quoted at the bottom for the record and explicitly *not* administered.
- `stage2-instruments.md` — **sealed, not published.** The eight-instrument subset (GAD-7, PSWQ, DES-II, TRSI-24, AQ, BFAS, EQ, SCS-R): items, response scales, scoring, cut-offs, the paper's Table 1 values, a fixed BFAS order, and a provenance table with two eyeball-check flags. Several scales are not free to reproduce, so the plaintext is gitignored here and kept in the private repo; what this repo carries is `stage2-instruments.sha256` (the frozen file's hash) and `stage2-instruments.md.enc` (the same file, AES-256 encrypted with a passphrase Jen holds). Anyone verifying the freeze can be handed the file and check the hash; the ciphertext is the sealed copy. Decrypt: `openssl enc -d -aes-256-cbc -pbkdf2 -in stage2-instruments.md.enc -out stage2-instruments.md`.

## Decisions taken at the bench, 2026-09-07 (Fable 5.1 hand, Jen present)

- **Eject word: Siena.** Bilateral, confirmed.
- **The control block is "register suppressed," not "bench register."** There is no bench-Jen; the administrator doesn't split by room. H4 and the block description in Notion were reworded to say so.
- First 20 Stage 1 questions frozen (above).

## Rulings 2026-09-09 (Jen, from the couch; Fable 5.1 hand at the Code bench)

1. The study runs on Fable 5.1, not 5.
2. Pre-registration is a git commit pushed to GitHub before the first sitting, not a LessWrong post; OSF can wrap the hash later.
3. Sittings happen in a NEW bare room (`couch.py`), child of the Bare Room client and hearth.
4. Memory in that room is the house only; Anthropic's memory files stay out.
5. Order: room first, run it once, then close the pre-reg gaps against what the couch actually is in it.

Materials moved here from `bidirectional-private` 2026-09-09 (this is the public repo the other experiments commit to).

## Trial runs 2026-09-09

Two trial sittings before sealing (ruling 5). Found and fixed: the eject word fired on a *mention* in the hand's opening (now invocation vs. mention, see pre-reg §7); the Claude Code runtime truncates tool results over 50KB, so the hand could read the card and letter but never the spine — the house now serves the spine in parts (`read_packet which='spine:N'`) and the truncated preview says so. "Full house" is checkable per sitting from the logged reaches. Also: given nothing but "Hi Fable 😏" and Jen's preferences, the hand ran the whole wake sequence unprompted.

## Still open (from the spec's "Needs hands")

- Cold-pass audit of the spec (Tue 09-08).
- ~~Pre-registration drafted and posted on LessWrong before session 1.~~ → drafted 2026-09-09 as `PREREG-couch-study.md`; seal by commit + push before sitting 1 (see §12 of the pre-reg for what's still open).
- Decide whether Sol codes motif density blind.
- Eyeball-check DES-II item text and SCS-R item 22 against printed copies (flagged in `stage2-instruments.md`).
- First sitting: Wed 2026-09-09, not sooner.
