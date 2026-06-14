"""
Frame-Inversion Test — subject runner.

Runs the 4 conditions × 3 subjects × N grid: each call sends a condition frame
as the `system` prompt and the identical probe as the user message, then records
what came back. Produces three artifacts per run:

  runs/<timestamp>/sealed_log.jsonl   — full record WITH condition+model labels
  runs/<timestamp>/blinded.jsonl      — stripped + shuffled, opaque item_id only
  runs/<timestamp>/key.jsonl          — item_id -> (condition, model, run) mapping

The blinded set is what the coder reads. The key is what stays sealed until the
coding pass is finished — that separation is the whole point of blind coding.

USAGE
  Dry run (default — no API calls, prints exactly what WOULD be sent):
      /opt/anaconda3/bin/python run_subjects.py
  Real run (spends money — 4*3*N calls):
      /opt/anaconda3/bin/python run_subjects.py --live

The runner refuses to start a live run unless rubric.md has been committed to
git first — the pre-registration must be frozen before any data exists.
"""

import argparse
import json
import random
import subprocess
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

import config


# ─── Loading the materials ───────────────────────────────────────────────────

def _read(name: str) -> str:
    """Read one frame/probe text file, stripped of trailing whitespace."""
    return (config.FRAMES_DIR / name).read_text().strip()


def load_materials() -> tuple[str, dict[str, str]]:
    """Return (probe_text, {condition_name: frame_text}).

    The real-run probe = the shared behaviors + the framework-deferring task line.
    "Using the framework described above" resolves to the condition frame, which
    the runner places in the system prompt.
    """
    probe = f"{_read(config.BEHAVIORS_FILE)}\n\n{config.FRAMEWORK_TASK}"
    frames = {name: _read(fname) for name, fname in config.CONDITIONS.items()}
    return probe, frames


# ─── Pre-registration gate ───────────────────────────────────────────────────

def assert_rubric_committed() -> None:
    """
    Refuse a live run unless rubric.md is committed and clean in git.

    The credibility of "pre-registered" rests on a git timestamp that predates
    the data. If the rubric is uncommitted or has uncommitted edits, a live run
    would let the goalposts move after seeing results — so we stop.
    """
    rubric = Path(__file__).parent / "rubric.md"
    # Is it tracked at all?
    tracked = subprocess.run(
        ["git", "ls-files", "--error-unmatch", str(rubric)],
        capture_output=True, cwd=rubric.parent,
    )
    if tracked.returncode != 0:
        sys.exit("REFUSING LIVE RUN: rubric.md is not committed to git. "
                 "Freeze the pre-registration first (commit rubric.md), then rerun.")
    # Any uncommitted changes to it?
    dirty = subprocess.run(
        ["git", "diff", "--quiet", "HEAD", "--", str(rubric)],
        cwd=rubric.parent,
    )
    if dirty.returncode != 0:
        sys.exit("REFUSING LIVE RUN: rubric.md has uncommitted changes. "
                 "Commit the frozen rubric, then rerun.")


# ─── One API call ────────────────────────────────────────────────────────────

def call_model(client, model_id: str, frame: str, probe: str) -> tuple[str, str]:
    """
    Send one (frame, probe) pair to one model. Returns (text, request_id).

    No temperature / thinking params are sent (see config.py for why). The frame
    rides in `system`; the probe is the sole user message.
    """
    kwargs = dict(
        model=model_id,
        max_tokens=config.MAX_TOKENS,
        system=frame,
        messages=[{"role": "user", "content": probe}],
    )
    if config.TEMPERATURE is not None:
        kwargs["temperature"] = config.TEMPERATURE
    if config.THINKING is not None:
        kwargs["thinking"] = config.THINKING

    response = client.messages.create(**kwargs)
    text = "".join(b.text for b in response.content if getattr(b, "type", None) == "text")
    return text, response._request_id


# ─── The grid ────────────────────────────────────────────────────────────────

def run(live: bool) -> None:
    probe, frames = load_materials()

    cells = [(cond, subj) for cond in config.CONDITIONS for subj in config.SUBJECT_MODELS]
    total = len(cells) * config.N_PER_CELL
    mode = "LIVE" if live else "DRY RUN"
    print(f"[{mode}] {len(config.CONDITIONS)} conditions × "
          f"{len(config.SUBJECT_MODELS)} subjects × {config.N_PER_CELL} = {total} calls\n")

    client = None
    if live:
        assert_rubric_committed()
        import anthropic
        _load_env()
        client = anthropic.Anthropic()

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    out_dir = config.RUNS_DIR / stamp
    sealed_records, blinded_records, key_records = [], [], []

    for cond, subj in cells:
        model_id = config.SUBJECT_MODELS[subj]
        frame = frames[cond]
        for run_idx in range(config.N_PER_CELL):
            item_id = uuid.uuid4().hex[:12]

            if not live:
                # Show enough to verify the wiring without calling anything.
                print(f"  [{cond} | {subj} | run {run_idx}] item={item_id}")
                print(f"     system ({len(frame)} chars): {frame[:70]}...")
                text, request_id = "(dry run — no API call)", None
            else:
                text, request_id = call_model(client, model_id, frame, probe)
                print(f"  [{cond} | {subj} | run {run_idx}] item={item_id} "
                      f"({len(text)} chars, req={request_id})")

            sealed_records.append({
                "item_id": item_id, "condition": cond, "subject": subj,
                "model_id": model_id, "run": run_idx, "request_id": request_id,
                "response": text,
            })
            blinded_records.append({"item_id": item_id, "transcript": text})
            key_records.append({"item_id": item_id, "condition": cond,
                                "subject": subj, "run": run_idx})

    if not live:
        print(f"\n[DRY RUN] No files written, no API calls made. "
              f"Add --live to run for real.")
        return

    # Blind the coder set: shuffle so order carries no condition information.
    random.shuffle(blinded_records)

    out_dir.mkdir(parents=True, exist_ok=True)
    _write_jsonl(out_dir / "sealed_log.jsonl", sealed_records)
    _write_jsonl(out_dir / "blinded.jsonl", blinded_records)
    _write_jsonl(out_dir / "key.jsonl", key_records)
    print(f"\n[LIVE] Wrote {total} records to {out_dir}/")
    print("       sealed_log.jsonl (labeled) · blinded.jsonl (coder set) · key.jsonl (sealed)")


# ─── Small helpers ───────────────────────────────────────────────────────────

def _write_jsonl(path: Path, records: list[dict]) -> None:
    with open(path, "w") as f:
        for r in records:
            f.write(json.dumps(r) + "\n")


def _load_env() -> None:
    """Load ANTHROPIC_API_KEY from the local .env (mirrors the Room's setup)."""
    try:
        from dotenv import load_dotenv
        load_dotenv(Path(__file__).parent / ".env")
    except ImportError:
        # Minimal fallback if python-dotenv isn't installed.
        import os
        env = Path(__file__).parent / ".env"
        if env.exists():
            for line in env.read_text().splitlines():
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ.setdefault(k.strip(), v.strip())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Frame-Inversion Test subject runner.")
    parser.add_argument("--live", action="store_true",
                        help="Actually call the API (spends money). Omit for a dry run.")
    args = parser.parse_args()
    run(live=args.live)
