
---

# 🟧 **README – `mini-api-fastapi`**

# ⚡ Mini API – FastAPI

Ce projet illustre une petite API REST construite avec **FastAPI**,  
destinée à montrer une architecture claire, documentée et maintenable.

L’API expose un CRUD simple (ex : gestion de tâches / contacts / items).

---

## 🚀 Objectifs

- Exposer une logique métier  
- Valider les données avec **Pydantic**  
- Fournir une documentation auto via **SwaggerUI**  
- Montrer des bonnes pratiques d'architecture simple

---

## 🧱 Stack & Outils

- FastAPI  
- Pydantic  
- Uvicorn  
- Python 3.10+

---

## 📂 Structure du projet

```

mini-api-fastapi/
│── app/
│   ├── main.py          # Point d'entrée de l'API
│   ├── models.py        # Modèles (si base de données)
│   ├── schemas.py       # Schémas Pydantic
│   └── routes/
│       └── items.py     # Routes / Endpoints
│── tests/               # (optionnel) Tests unitaires
│── requirements.txt
└── README.md


```

---

## ▶️ Lancer l’API

```bash
- pip install -r requirements.txt
- uvicorn app.main:app --reload

```
## 📚 Documentation

Une fois l’API lancée :
- Swagger : http://localhost:8000/docs
- ReDoc : http://localhost:8000/redoc

## 📈 Améliorations prévues

- Ajout d’une base de données SQLite
- Authentification simple (JWT ou OAuth2)
- Ajout d’un Dockerfile pour déploiement rapide
- Tests unitaires (pytest)

## 📬 Contact

- Email : diawaramantcha@gmail.com
- LinkedIn : @mantcha-diawara
