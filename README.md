# ChatBot_IA

## Description

Projet réalisé dans le cadre du stage Data & IA chez Alten.

Objectif ::
Développer un chatbot IA capable de comprendre une question en langage naturel, de la convertir en requête SQL, d'interroger une base de données RH puis de retourner la réponse de manière claire.

---

## Structure du projet

```
ChatBot_IA/
│
├── config/
├── data/
├── ingestion/
├── traitement/
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── README.md
```

---

## Installation

Créer l'environnement

```bash
py -m venv venv
```

Activer

```bash
.\venv\Scripts\Activate.ps1
```

Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## Exécuter les tests

```bash
pytest
```