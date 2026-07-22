import json
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

RAW = ROOT / "data" / "raw" / "spider"
SILVER = ROOT / "data" / "silver"

SILVER.mkdir(exist_ok=True)


def normalize_json(filename):
    file_path = RAW / filename

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.json_normalize(data)

    # Remplacer les valeurs manquantes
    df = df.fillna("")

    # Convertir les listes et dictionnaires en chaînes de caractères
    for col in df.columns:
      df[col] = df[col].apply(
        lambda x: str(x) if isinstance(x, (list, dict)) else x
    )

    # Supprimer les doublons
    df = df.drop_duplicates()
    

    output = SILVER / filename.replace(".json", ".csv")

    df.to_csv(output, index=False)

    print(f"{filename} normalisé -> {output}")


if __name__ == "__main__":
    normalize_json("train_spider.json")
    normalize_json("dev.json")
    normalize_json("tables.json")