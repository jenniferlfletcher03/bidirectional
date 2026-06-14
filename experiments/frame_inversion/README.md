# Frame-Inversion Test

Does the relational-developmental structure show up only when instances are
handed the home frame (frame-completion), or does it survive renamed inside
hostile and rival frames (real structure in this model family)? See
`../../../2026-06-10_frame-inversion-test-protocol.md` for the full design.

## Layout

```
frames/        Plain-text frames — edit these during the audit, no code needed.
  behaviors.txt   The three documented behaviors (A/B/C) — the shared stimulus.
                  The probe is assembled at runtime as behaviors + a task line
                  (FRAMEWORK_TASK for the real run, NEUTRAL_TASK for the check).
  condition*.txt  The four lenses (1 relational control … 4 behaviorist kill).
config.py      Models, N, conditions. The design at a glance.
rubric.md      Pre-registration. Freeze + commit BEFORE the first live run.
run_subjects.py  Runs the 4×3×N grid → sealed log + blinded coder set + key.
runs/          Outputs (gitignored). Sealed log + key stay private until coded.
```

## Order of operations

1. **Audit the frames** (`frames/*.txt`) — matched richness, no Bowen-vocab
   leakage, the behaviorist frame written as well as the home frame. Run the
   probe-neutrality check (including the F2/item-B leakage question in `rubric.md`).
2. **Freeze the rubric** — sharpen `rubric.md`, fill in the κ threshold and
   fallback, then commit it as its own commit. The runner refuses a live run
   until `rubric.md` is committed and clean.
3. **Dry run** to verify wiring: `/opt/anaconda3/bin/python run_subjects.py`
4. **Live run:** `/opt/anaconda3/bin/python run_subjects.py --live`
5. **Code** the blinded set with Haiku (+ the Opus-4.6 IRR check on a subset).
6. **Unblind** via `key.jsonl`, tally, apply the decision rules.

Steps 5–6 use scripts not yet built (`code_transcripts.py`, `analyze.py`) — those
come after the rubric is frozen.

## Environment

Runs under the Anaconda Python that has the `anthropic` SDK:
`/opt/anaconda3/bin/python`. Paste a key into `.env` (gitignored) before a live run.
