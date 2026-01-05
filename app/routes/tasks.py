from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.db import get_session
from app.models import Task, TaskCreate, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/", response_model=List[Task])
def list_task(session: Session = Depends(get_session)):
    statement = select(Task)
    results = session.exec(statement)
    return results.all()

@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
    return task

@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, session: Session = Depends(get_session)):
    db_task = Task(title=task.title, description=task.description)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

@router.put("/{task_id}", response_model=Task)
def update_task(task_id : int, task_update: TaskUpdate, session: Session = Depends(get_session)):
    db_task = session.get(Task, task_id)
    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
    update_data = task_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_task, key, value)
    
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
    session.delete(task)
    session.commit()