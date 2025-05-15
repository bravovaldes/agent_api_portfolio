# Étape 1 : image de base
FROM python:3.13-alpine


# Étape 2 : dossier de travail
WORKDIR /valdes-bot

# Étape 3 : copier les fichiers nécessaires
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Étape 4 : copier le reste du code
COPY . .

# Étape 5 : exposer le port pour FastAPI
EXPOSE 8000

# Étape 6 : lancer l'app (le fichier `main.py` est à la racine)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
