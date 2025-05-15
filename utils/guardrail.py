FORBIDDEN_TOPICS = ["politique", "cinéma", "sport", "religion", "chatgpt", "météo", "musique"]

def is_valid_question(question: str) -> bool:
    q = question.lower()
    return not any(t in q for t in FORBIDDEN_TOPICS)
