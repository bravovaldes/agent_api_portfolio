FROM python:3.11

# Installer les dépendances système
RUN apt-get update && apt-get install -y build-essential python3-dev

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .

# Mettre à jour pip et installer les dépendances Python
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code
COPY . .


# Étape 5 : exposer le port pour FastAPI
EXPOSE 8000

# Étape 6 : lancer l'app (le fichier `main.py` est à la racine)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
