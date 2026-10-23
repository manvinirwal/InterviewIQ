# interview_bank.py
# A small bank of behavioral + technical interview questions,
# each tagged with a category and the concepts a strong answer
# should mention. Feel free to add your own questions here.

QUESTIONS = [
    {
        "category": "behavioral",
        "question": "Tell me about a time you had to debug a difficult production issue.",
        "expected_keywords": ["logs", "root cause", "monitoring", "rollback", "team"],
    },
    {
        "category": "behavioral",
        "question": "Describe a situation where you disagreed with a teammate. How did you handle it?",
        "expected_keywords": ["communication", "compromise", "feedback", "listened"],
    },
    {
        "category": "technical",
        "question": "Walk me through how you would design a URL shortener.",
        "expected_keywords": ["hashing", "database", "scalability", "cache", "collision"],
    },
    {
        "category": "technical",
        "question": "How would you design a rate limiter for a public API?",
        "expected_keywords": ["throttling", "token bucket", "redis", "latency", "quota"],
    },
    {
        "category": "behavioral",
        "question": "Tell me about a time you had to learn a new technology quickly to finish a project.",
        "expected_keywords": ["documentation", "deadline", "prototype", "mentor", "practice"],
    },
]
