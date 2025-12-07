# app/routes/items.py
from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["items"],
)

# Pour le moment, on simule une "base de données" vide
fake_items_db = []

@router.get("/")
def list_items():
    """
    Récupère la liste des tâches.
    Pour l'instant, renvoie une liste vide ou des données en dur.
    """
    return fake_items_db

@router.post("/")
def create_item(item: TaskCreate):