# tools.py 
# ============================================================
#  Three rule-based evaluation "tools" the agent can call.
#  Each returns a structured dict (not a pre-formatted string) --
#  the agent decides how to present it to the model and uses the
#  raw numbers later for the final-report aggregation.
# ============================================================

FILLER_WORDS = ["um", "uh", "like", "basically", "actually", "you know", "so yeah", "i mean"]


def detect_filler_words(answer: str) -> dict:
    """Count filler words (um, like, basically, etc.) in a candidate's answer."""
    text = answer.lower()
    found = {w: text.count(w) for w in FILLER_WORDS if text.count(w) > 0}
    total = sum(found.values())
    return {
        "total": total,
        "found": found,
        "verdict": "clean" if total <= 2 else "needs improvement",
    }


STAR_SIGNALS = {
    "situation": ["when", "at my", "in my previous", "while working", "during"],
    "task": ["i needed to", "my task", "i was responsible", "the goal was", "i had to"],
    "action": ["i decided", "i implemented", "i built", "i led", "i created", "i took"],
    "result": ["as a result", "this led to", "we achieved", "the outcome", "ended up", "improved", "increased", "reduced"],
}


def check_star_structure(answer: str) -> dict:
    """Check whether a behavioral answer covers Situation, Task, Action, Result."""
    text = answer.lower()
    # this creates a dict of stages and whether any of the signals for that stage are present in the answer(T/F)
    present = {stage: any(sig in text for sig in signals) for stage, signals in STAR_SIGNALS.items()}
    # this creates a list of stages that are not present in the answer
    missing = [stage for stage, ok in present.items() if not ok]
    return {
        "present": present,
        "missing": missing,
        "all_present": not missing, # false if any stage is missing, true if all stages are present
    }


def score_relevance(answer: str, expected_keywords: list) -> dict:
    """Score how many expected_keywords appear in the answer."""
    text = answer.lower()
    covered = [kw for kw in expected_keywords if kw.lower() in text]
    missed = [kw for kw in expected_keywords if kw.lower() not in text]
    score = round(100 * len(covered) / len(expected_keywords)) if expected_keywords else 0
    return {
        "score": score,
        "covered": covered,
        "missed": missed,
    }
