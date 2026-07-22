import pandas as pd
from pathlib import Path
from datetime import datetime
import os

# Racine du projet
ROOT = Path(__file__).resolve().parent.parent

# Dossiers
SILVER = ROOT / "data" / "silver"
LOG_DIR = ROOT / "data" / "logs"

# Création automatique du dossier logs
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Fichier du rapport
REPORT = LOG_DIR / "quality_report.txt"

files = [
    "train_spider.csv",
    "dev.csv",
    "tables.csv"
]

# Colonnes critiques pour le contrôle qualité
required_columns = ["question", "query", "db_id"]

total_files = 0
valid_files = 0
total_alerts = 0

with open(REPORT, "w", encoding="utf-8") as report:

    report.write("===== RAPPORT QUALITE DES DONNEES =====\n\n")

    for file in files:

        total_files += 1

        file_path = SILVER / file

        if not file_path.exists():
            report.write(f"Fichier introuvable : {file}\n")
            total_alerts += 1
            report.write("\n---------------------------\n\n")
            continue

        df = pd.read_csv(file_path)

        report.write(f"Fichier : {file}\n")
        report.write(f"Nombre de lignes : {len(df)}\n")
        report.write(f"Nombre de colonnes : {len(df.columns)}\n")

        # ==================================================
        # COMPLETUDE
        # ==================================================

        if all(col in df.columns for col in required_columns):

            missing_values = df[required_columns].isnull().sum().sum()
            total_values = df[required_columns].size

            report.write(
                "Colonnes critiques vérifiées : question, query, db_id\n"
            )

        else:

            missing_values = df.isnull().sum().sum()
            total_values = df.size

            report.write(
                "Colonnes critiques absentes, contrôle sur toutes les colonnes.\n"
            )

        completeness = 0

        if total_values > 0:
            completeness = (missing_values / total_values) * 100

        report.write(f"Valeurs manquantes : {missing_values}\n")
        report.write(f"Taux de valeurs manquantes : {completeness:.2f}%\n")

        if completeness > 5:
            report.write("ALERTE : Complétude insuffisante (>5%)\n")
            total_alerts += 1
        else:
            report.write("Complétude : OK\n")

        # ==================================================
        # UNICITE
        # ==================================================

        duplicates = df.duplicated().sum()

        uniqueness = 0

        if len(df) > 0:
            uniqueness = (duplicates / len(df)) * 100

        report.write(f"Doublons : {duplicates}\n")
        report.write(f"Taux de doublons : {uniqueness:.2f}%\n")

        if uniqueness > 1:
            report.write("ALERTE : Trop de doublons (>1%)\n")
            total_alerts += 1
        else:
            report.write("Unicité : OK\n")

        # ==================================================
        # FRAICHEUR
        # ==================================================

        last_modified = datetime.fromtimestamp(os.path.getmtime(file_path))
        age_days = (datetime.now() - last_modified).days

        report.write(f"Âge du fichier : {age_days} jours\n")

        if age_days > 365:
            report.write("ALERTE : Dataset ancien (>365 jours)\n")
            total_alerts += 1
        else:
            report.write("Fraîcheur : OK\n")

        # ==================================================
        # FICHIER VIDE
        # ==================================================

        if len(df) == 0:
            report.write("ALERTE : Fichier vide\n")
            total_alerts += 1
        else:
            valid_files += 1

        report.write("\n---------------------------\n\n")

    # ==================================================
    # RESUME FINAL
    # ==================================================

    report.write("========== RESUME ==========\n")
    report.write(f"Fichiers analysés : {total_files}\n")
    report.write(f"Fichiers valides : {valid_files}\n")
    report.write(f"Alertes : {total_alerts}\n")

    if total_alerts == 0:
        report.write("Qualité globale : OK\n")
    else:
        report.write("Qualité globale : Des anomalies ont été détectées\n")

print("Rapport généré :", REPORT)