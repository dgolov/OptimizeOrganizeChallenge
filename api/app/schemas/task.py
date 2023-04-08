from pydantic import BaseModel
from datetime import datetime


class TaskBase(BaseModel):
    deadline: datetime
    description: str
    responsible: str
    work_group_id: int
    solution_id: int
    object_id: int
    created_at: datetime
    updated_at = datetime

    class Config:
        orm_mode = True


class TaskSchema(TaskBase):
    id: int


class CreateTask(TaskBase):
    pass

