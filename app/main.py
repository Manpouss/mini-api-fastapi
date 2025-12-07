# app/main.py
from fastapi import FastAPI
from app.routes import items

# On crée l'application FastAPI
app = FastAPI(
    title="Mini API - Gestion de tâches",
    description="Une petite API FastAPI pour gérer des tâches (ToDo).",
    version="0.1.0",
)

# On inclut les routes définies dans app/routes/items.py
app.include_router(items.router)

# Route de base pour vérifier que l'API fonctionne
@app.get("/")
def read_root():
    return {"message": "API de gestion de tâches - OK"}
