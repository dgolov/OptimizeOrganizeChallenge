from pydantic import BaseModel
from datetime import datetime


class TaskBase(BaseModel):
    id: int
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



class CreateTask(TaskBase):
    pass

