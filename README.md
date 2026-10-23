# InterviewIQ -- Solution (Instructor Reference)


## Setup 
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate then paste your API keys 

pip3 install -r requirements.txt or python3 -m pip install -r requirements.txt

```

## Ways to run it
```bash
python main.py            # CLI walkthrough
python memory_check.py    # scripted memory/aggregation check -- see below
python app.py              # the required Gradio interface, opens in your browser
python run_multi_agent.py  #  two-agent (Interviewer + Evaluator) mode
```
See `sample_session_output.txt` for an example transcript (CLI run + the
memory_check.py meta-question) without needing to run anything live.

## Files
| File | What it is |
|---|---|
| `interview_bank.py` | Sample interview questions + expected keywords. |
| `tools.py` | Fully implemented: `detect_filler_words`, `check_star_structure`, `score_relevance` -- each returns a dict. |
| `agent.py` | Fully implemented tool-calling agent: session memory, a final report that aggregates and names the weakest area, and `ask_agent` for free-form meta-questions. |
| `main.py` | CLI runner. |
| `memory_check.py` | Scripted mini-session (one strong answer, one weak one, then a meta-question) that proves memory/aggregation is working -- the weakest area named should be the weak answer's question, not the most recent one. |
| `app.py` | The Gradio interface -- question flow, live scorecard, an "ask the coach" box for meta-questions, and a final-report button. |
| `sample_session_output.txt` | Example run transcript, for reference/demo without live API calls. |
| `interviewer_agent.py`, `run_multi_agent.py` : a second "Interviewer" agent that picks the next question's category, handed off to the (unchanged) Evaluator agent by a small orchestrator loop.
| `requirements.txt`, `.env.example`, `.gitignore` 
| `Problem_Statement_and_Milestones.md` for what each one does. |


## Area of Improvement

1. Backend API: Use FastAPI for creating interviews, submitting answers, and fetching reports.
2. Database: Store interviews, answers, and scores in SQLite or PostgreSQL so users can revisit sessions.
3. Session isolation: Keep each user’s interview state separate. Current global session memory could mix users’ data.
4. Tests and error handling: Test scoring logic and handle invalid inputs, API timeouts, and failed responses.
5. Deployment: Provide a runnable demo with clear setup instructions; Docker would help make setup reproducible.

