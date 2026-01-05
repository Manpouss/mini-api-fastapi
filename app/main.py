# app/main.py
from fastapi import FastAPI
from app.routes import tasks
from app.db import create_db_and_tables

# On crée l'application FastAPI
app = FastAPI(
    title="Mini API - Gestion de tâches",
    description="Une petite API FastAPI pour gérer des tâches (ToDo).",
    version="0.2.0",
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()



# On inclut les routes définies dans app/routes/items.py
app.include_router(tasks.router)

# Route de base pour vérifier que l'API fonctionne
@app.get("/")
def read_root():
    return {"message": "API de gestion de tâches - OK"}
