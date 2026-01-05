from typing import Optional
from sqlmodel import Field, SQLModel

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None

class TaskCreate(SQLModel):
    title: str
    description: Optional[str] = None

class TaskUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None