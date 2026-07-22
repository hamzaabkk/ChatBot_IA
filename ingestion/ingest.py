import shutil
from pathlib import Path

from logger import logger
from config import RAW_DIR


def ingest_dataset(source_folder: str):
    source = Path(source_folder)

    if not source.exists():
        logger.error(f"Dossier introuvable : {source}")
        raise FileNotFoundError(source)

    destination = RAW_DIR / source.name

    if destination.exists():
        shutil.rmtree(destination)

    shutil.copytree(source, destination)

    logger.info(f"Dataset copié vers {destination}")


if __name__ == "__main__":
    ingest_dataset("spider")