from pydantic import BaseModel
from datetime import datetime


class TaskBase(BaseModel):
    deadline: datetime
    description: str
    responsible: str
    work_group_id: int
    solution_id: int
    object_id: int

    class Config:
        orm_mode = True


class TaskSchema(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime


class UpdateTask(TaskBase):
    updated_at: datetime = datetime.utcnow()

    class Config:
        validate_assignment = True


class CreateTask(UpdateTask):
    created_at: datetime = datetime.utcnow()

