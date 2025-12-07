class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    done: bool = False

