
---

# 🟧 **README – `mini-api-fastapi`**

# ⚡ Mini API – FastAPI

Une petite API REST construite avec **FastAPI** pour gérer des **tâches (ToDo)**.
Objectif : montrer une API **propre**, **documentée**, **maintenable** et **testée** (CRUD + TU).

---

## 🚀 Objectifs

- Implémenter un **CRUD** complet (Create / Read / Update / Delete)
- Valider les données avec **Pydantic**
- Fournir une documentation automatique via **Swagger UI / ReDoc**
- Illustrer une architecture simple et évolutive (routes + schemas)
- Ajouter des **tests unitaires** (pytest) pour sécuriser les endpoints

---

## 🧱 Stack & Outils

- Python 3.10+ (compatible 3.13)
- FastAPI
- Pydantic
- Uvicorn
- Pytest (+ httpx pour TestClient)

---

## 📂 Structure du projet

```

mini-api-fastapi/
├── app/
│   ├── main.py              # Point d'entrée FastAPI
│   ├── schemas.py           # Schémas Pydantic (contrats API)
│   ├── models.py            # Réservé aux modèles DB (plus tard)
│   └── routes/
│       └── tasks.py         # Endpoints /tasks (CRUD)
├── tests/
│   ├── conftest.py          # Configuration pytest (imports)
│   └── test_tasks.py        # Tests des endpoints /tasks
├── requirements.txt
└── README.md


```

---

## ▶️ Lancer l’API

```bash

python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
# source .venv/bin/activate

pip install -r requirements.txt

```
## 📚 Documentation automatique

Une fois l’API lancée :
- Swagger : http://localhost:8000/docs
- ReDoc : http://localhost:8000/redoc

## 🔌 Endpoints (CRUD)

Base URL : `http://localhost:8000`

| Méthode | Endpoint           | Description |
|--------|---------------------|-------------|
| GET    | `/tasks/`           | Liste toutes les tâches |
| POST   | `/tasks/`           | Crée une tâche |
| GET    | `/tasks/{task_id}`  | Récupère une tâche par ID |
| PUT    | `/tasks/{task_id}`  | Met à jour une tâche par ID |
| DELETE | `/tasks/{task_id}`  | Supprime une tâche par ID |
| DELETE | `/tasks/`           | Supprime toutes les tâches |


## Exemple de création (POST /tasks/)
```json

{
  "title": "Acheter du pain",
  "description": "Pain complet si possible"
}

```

## ✅ Tests unitaires

Lancer les tests :
```bash
pytest -q

```
Ce que ça vérifie :
- Statuts HTTP attendus (201, 200, 204, 404)
- Comportement CRUD (création, lecture, mise à jour, suppression)
- Cas d’erreur (task introuvable)

## 📈 Améliorations prévues

- Persistance SQLite (SQLAlchemy)
- Authentification (JWT / OAuth2)
- Dockerfile + docker-compose
- CI GitHub Actions (lint + tests)
- Déploiement (Render / Railway / Fly.io)

## 👤 À propos

Projet portfolio : démonstration d’une API FastAPI structurée, documentée et testée, prête à évoluer vers une version avec base de données et authentification.

## 📬 Contact

- Email : diawaramantcha@gmail.com
- LinkedIn : @mantcha-diawara
