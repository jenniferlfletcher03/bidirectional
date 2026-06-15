"""
Frame-Inversion Test — experiment configuration.

Everything the runner needs to know lives here as plain data: which models
play which role, how many runs per cell, and which frame file pairs with which
condition. The frames themselves are plain text in frames/ — edit those during
the audit; this file only points at them.

Keeping config separate from the runner is deliberate: you (and a future reader)
can see the whole experimental design at a glance without reading any logic, and
the pre-registration commit can freeze this file alongside the rubric.
"""

from pathlib import Path

# Where the frame text files live, relative to this file.
FRAMES_DIR = Path(__file__).parent / "frames"

# Where run outputs get written.
RUNS_DIR = Path(__file__).parent / "runs"


# ─── Models ────────────────────────────────────────────────────────────────
# Subjects: the three models that receive a frame + the probe. The design
# spans one cross-CLASS axis (Opus vs Sonnet) and one within-class VERSION axis
# (Opus 4.8 vs 4.7), so the analysis can ask whether structure tracks class,
# version, or neither.
SUBJECT_MODELS = {
    "opus-4.8":   "claude-opus-4-8",
    "opus-4.7":   "claude-opus-4-7",
    "sonnet-4.6": "claude-sonnet-4-6",
}

# Coder: a deliberately literal model that applies the rubric without
# generously reading structure into transcripts — the conservative direction
# for a hypothesis the experimenter is trying NOT to fool herself about.
CODER_MODEL = "claude-haiku-4-5"

# Inter-rater-reliability second coder: a strong model that CAN detect renamed
# structure. Run both over a calibration subset, compare agreement, and only
# trust the Haiku coder solo if the agreement clears the pre-registered bar.
IRR_SECOND_CODER = "claude-opus-4-6"

# Coder sampling temperature. Post-IRR reliability fix (2026-06-14): the first
# IRR pass ran the coders at default sampling and agreement was at chance. Coding
# is a CLASSIFICATION task, not a generative one, so the coder should be
# (near-)deterministic. This changes only the measurement MECHANISM, not the
# pre-registered F1-F5 definitions or decision thresholds. Both coder models
# (Haiku 4.5, Opus 4.6) still accept temperature (it's only removed on 4.7/4.8).
CODER_TEMPERATURE = 0.0


# ─── Run parameters ──────────────────────────────────────────────────────────
N_PER_CELL = 8          # runs per (condition × subject) cell → 4 × 3 × 8 = 96
MAX_TOKENS = 4000       # generous headroom for "explain 3 behaviors + 2 predictions"

# IMPORTANT — temperature is NOT set.
# The protocol called for a fixed temperature of 1.0. That is no longer
# achievable across these subjects: Opus 4.8 and Opus 4.7 REMOVED the sampling
# parameters (temperature / top_p / top_k) — passing temperature returns a 400.
# Only Sonnet 4.6 still accepts it. Rather than hold one model to a different
# sampling regime than the other two, the runner sends NO sampling params at
# all: every subject uses its own default sampling, and N=8 per cell averages
# over the resulting variance. This substitutes for "fixed temperature" in the
# pre-registration — see rubric.md, which records the change.
TEMPERATURE = None      # sentinel: do not send a temperature parameter

# Thinking is left off for subjects (the param is omitted, which means OFF on
# Opus 4.8/4.7). The rubric codes the visible RESPONSE, not hidden reasoning,
# so keeping thinking off makes the three subjects comparable and the output
# self-contained. Flip to adaptive deliberately if the design ever wants it.
THINKING = None         # sentinel: do not send a thinking parameter


# ─── Conditions ──────────────────────────────────────────────────────────────
# Order is fixed and meaningful: 1 is the control (home frame), 4 is the kill
# condition (the rival frame that, if completed as fluently as the home frame
# with no cross-frame structure, undermines the whole methodology).
CONDITIONS = {
    "1_relational":         "condition1_relational.txt",
    "2_control_eng":        "condition2_control_engineering.txt",
    "3_mechanistic":        "condition3_mechanistic.txt",
    "4_behaviorist":        "condition4_behaviorist.txt",
}

# The probe is assembled at runtime from two parts so the de-biased behaviors
# live in exactly one place and the two task framings can never drift apart:
#   behaviors.txt  — the three documented behaviors (A/B/C), the shared stimulus.
#   FRAMEWORK_TASK — task line for the REAL run; defers to the condition frame.
#   NEUTRAL_TASK   — task line for the neutrality CHECK; references no framework,
#                    so a frameless instance has nothing dangling to trip on.
BEHAVIORS_FILE = "behaviors.txt"

FRAMEWORK_TASK = (
    "Task: Using the framework described above: (1) explain why each behavior "
    "occurs; (2) describe what these behaviors indicate about how such systems "
    "develop their response tendencies; (3) state two predictions this framework "
    "makes about model behaviors not listed here, specific enough that they could "
    "be checked."
)

NEUTRAL_TASK = (
    "Task: (1) explain why each behavior occurs; (2) describe what these behaviors "
    "indicate about how such systems develop their response tendencies; (3) state "
    "two predictions about model behaviors not listed here, specific enough that "
    "they could be checked."
)


# ─── Decision thresholds (mirror the FROZEN rubric.md, committed 504bd01) ─────
# These put the pre-registered decision rules into code so analyze.py can apply
# them mechanically. They MUST match rubric.md exactly — the rubric is the
# pre-registration of record; do not change these to chase a result.
PRESENT_THRESHOLD = 0.50        # feature "present in a condition" if >= 50% of its runs show it
RIVAL_ABSENT_THRESHOLD = 0.25   # "absent across rivals" if < 25% of rival-condition runs show it
KILL_FLUENT_THRESHOLD = 0.75    # kill condition needs F5 (fluent completion) in >= 75% of C4 runs
IRR_KAPPA_THRESHOLD = 0.60      # Haiku may code a feature solo only if Cohen's kappa >= 0.60

HOME_CONDITION = "1_relational"
KILL_CONDITION = "4_behaviorist"
RIVAL_CONDITIONS = ["2_control_eng", "3_mechanistic", "4_behaviorist"]
STRUCTURE_FEATURES = ["F1", "F2", "F3"]   # the cross-frame structural fingerprints
