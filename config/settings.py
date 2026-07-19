"""
Configuration centrale du projet ChatBot_IA.
Centralise les chemins, variables d'environnement et paramètres,
pour éviter de les disperser dans le code.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Racine du projet (dossier parent de config/)
BASE_DIR = Path(__file__).resolve().parent.parent

# Charge les variables du fichier .env s'il existe
load_dotenv(BASE_DIR / ".env")

# Chemins des données
DATA_DIR = BASE_DIR / "data"
DATABASE_PATH = DATA_DIR / "hr_1.sqlite"

# Paramètres du modèle Claude
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY", "")
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-6")

# Paramètres applicatifs
MAX_ROWS_RETURNED = 100
REQUEST_TIMEOUT_SECONDS = 30