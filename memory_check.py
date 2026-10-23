# memory_check.py
# ============================================================
#  A scripted mini-session that exercises session memory.
#  Two answers are scored -- one clearly strong, one clearly
#  weak -- then a meta-question is asked that can only be
#  answered correctly by looking back at BOTH turns, not just
#  the most recent one.
#
#  Run this against your own agent.py once Ask 1 and Ask 2 are
#  done:
#      python memory_check.py
#
#  Read the transcript it prints and confirm:
#    1. The relevance scores reported for each turn look right
#       given the two answers below.
#    2. The "weakest area" the coach names is the WEAK_ANSWER's
#       question -- not whichever question was asked most
#       recently. If it names the wrong one, your memory or your
#       aggregation logic is only looking at the last turn.
# ============================================================

from agent import run_turn, ask_agent

STRONG_ANSWER = (
    "When our checkout service started throwing errors at 2am, I was "
    "responsible for figuring out what broke. I led the investigation, "
    "checked the logs, and found the root cause was a bad deployment. My "
    "team and I performed a rollback, and as a result we restored service "
    "within 20 minutes and added better monitoring afterward."
)
# When our checkout service started throwing errors at 2am, I was responsible for figuring out what broke. I led the investigation, checked the logs, and found the root cause was a bad deployment. My team and I performed a rollback, and as a result we restored service within 20 minutes and added better monitoring afterward.
STRONG_KEYWORDS = ["logs", "root cause", "monitoring", "rollback", "team"]
STRONG_QUESTION = "Tell me about a time you had to debug a difficult production issue."

WEAK_ANSWER = "So, um, basically I just kind of, like, tried a few things until it worked, I guess."
WEAK_KEYWORDS = ["communication", "compromise", "feedback", "listened"]
WEAK_QUESTION = "Describe a situation where you disagreed with a teammate. How did you handle it?"

if __name__ == "__main__":
    print("Turn 1 (strong answer) ->")
    print(run_turn(STRONG_QUESTION, STRONG_ANSWER, STRONG_KEYWORDS))

    print("\nTurn 2 (weak answer) ->")
    print(run_turn(WEAK_QUESTION, WEAK_ANSWER, WEAK_KEYWORDS))

    print("\nMeta-question: 'What is my weakest area so far, and why?' ->")
    print(ask_agent("What is my weakest area so far, and why?"))
