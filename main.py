from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from utils.guardrail import is_valid_question
from utils.rag import load_vectorstore
from openai import OpenAI
import os

# Charger les variables d'environnement
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialiser FastAPI
app = FastAPI()

# Charger la base vectorielle (ChromaDB)
vectorstore = load_vectorstore()

# Modèle de la requête
class AskRequest(BaseModel):
    question: str

@app.post("/ask")
def ask(req: AskRequest):
    if not is_valid_question(req.question):
        return {
            "answer": "Je suis uniquement conçu pour répondre à des questions sur Valdes Mezankou Bravo et son parcours professionnel."
        }

    # Récupérer les documents les plus pertinents
    docs = vectorstore.similarity_search(req.question, k=3)
    context = "\n\n".join([d.page_content for d in docs])

    # Créer la requête pour le modèle GPT
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Tu es un assistant qui répond uniquement à propos de Valdes Mezankou Bravo, son expérience, ses compétences, et ses projets."
            },
            {
                "role": "user",
                "content": f"Contexte :\n{context}\n\nQuestion : {req.question}"
            }
        ],
        temperature=0.4
    )

    return {
        "answer": response.choices[0].message.content.strip()
    }
