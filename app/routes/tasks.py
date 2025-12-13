from fastapi import APIRouter, status, HTTPException
from app.schemas import TaskCreate, TaskResponse, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["tasks"])

fake_tasks_db: list[dict] = []

def _get_task_index(task_id: int) -> int:
    """Retourne l'index de la tâche dans fake_tasks_db, ou -1 si introuvable."""
    for i, task in enumerate(fake_tasks_db):
        if task["id"] == task_id:
            return i
    return -1

@router.get("/", response_model=list[TaskResponse])
def list_tasks():
    return fake_tasks_db

@router.get("/{task_id}", response_model=TaskResponse)
def get_task_by_id(task_id: int):
    idx = _get_task_index(task_id)
    if idx == -1:
        raise HTTPException(status_code=404, detail="Task not found")
    return fake_tasks_db[idx]

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    new_task = {
        "id": len(fake_tasks_db) + 1,
        "title": task.title,
        "description": task.description,
    }
    fake_tasks_db.append(new_task)
    return new_task

@router.put("/{task_id}", response_model=TaskResponse)
def update_task_by_id(task_id: int, payload: TaskUpdate):
    idx = _get_task_index(task_id)
    if idx == -1:
        raise HTTPException(status_code=404, detail="Task not found")

    task = fake_tasks_db[idx]

    # On met à jour seulement les champs fournis (non None)
    if payload.title is not None:
        task["title"] = payload.title
    if payload.description is not None:
        task["description"] = payload.description
    if payload.done is not None:
        task["done"] = payload.done

    fake_tasks_db[idx] = task
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task_by_id(task_id: int):
    idx = _get_task_index(task_id)
    if idx == -1:
        raise HTTPException(status_code=404, detail="Task not found")
    fake_tasks_db.pop(idx)
    return None

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_all_tasks():
    fake_tasks_db.clear()
    return None