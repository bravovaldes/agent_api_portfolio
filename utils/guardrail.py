FORBIDDEN_TOPICS = [
    "politique", "élections", "gouvernement", "président",
    "cinéma", "film", "acteur", "actrice", "série",
    "sport", "match", "football", "nba", "ligue", "joueur",
    "religion", "dieu", "islam", "christianisme", "judaïsme",
    "chatgpt", "gpt", "openai",
    "météo", "temps qu'il fait", "climat",
    "musique", "chanson", "artiste", "album"
]

def is_valid_question(question: str) -> bool:
    q = question.lower()
    return not any(topic in q for topic in FORBIDDEN_TOPICS)
