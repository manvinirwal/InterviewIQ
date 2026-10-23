# interviewer_agent.py -- Ask 4 (optional bonus): a second, specialized agent
# ============================================================
#  InterviewIQ -- Two-Agent Extension
#  This is given fully worked, not a TODO file -- it goes beyond
#  what the six classes covered hands-on (multi-agent was only
#  introduced as vocabulary in Class 6's guide: an "orchestrator"
#  coordinating "specialized agents"). Read it, run it, and feel
#  free to extend it -- there's nothing to fill in.
#
#  This agent has ONE job: given how the candidate has done so
#  far, decide whether the NEXT question should be "behavioral"
#  or "technical". It does not evaluate answers -- that's still
#  the Evaluator agent's job in agent.py, completely unchanged.
#
#  Kept deliberately simple: no A2A protocol, no agent cards, no
#  network calls between agents -- just a second agent with its
#  own system prompt, called in sequence by a small orchestrator
#  (run_multi_agent.py). That's the "orchestrator + specialized
#  agents" pattern from Class 6's multi-agent slide, minimal.
# ============================================================

import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

load_dotenv(find_dotenv(), override=True)

PROVIDER = "groq"   # "groq" (free) or "openai"

if PROVIDER == "groq":
    MODEL = "openai/gpt-oss-20b"
    client = OpenAI(api_key=os.getenv("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1")
else:
    MODEL = "gpt-4o-mini"
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """You are the Interviewer half of InterviewIQ's two-agent mock interview system.
Your only job: decide whether the NEXT question should be "behavioral" or "technical",
based on how the candidate has done so far.
Rule of thumb: after a weak answer, consider staying in the same category so the
candidate can try again; after a strong answer, feel free to switch categories to
test breadth. Respond with exactly one word: behavioral or technical."""


def choose_next_category(session_summary: str) -> str:
    """Ask the Interviewer agent to pick the next question's category.

    `session_summary` is a short plain-English recap of performance so far
    (e.g. agent.generate_final_report()'s output) -- pass "" for the very
    first question of the session.
    """
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": session_summary or "This is the first question of the session. Pick a category to start with."},
    ]
    response = client.chat.completions.create(model=MODEL, messages=messages)
    choice = response.choices[0].message.content.strip().lower()
    return "technical" if "technical" in choice else "behavioral"
