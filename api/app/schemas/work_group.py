from pydantic import BaseModel
from datetime import datetime


class WorkGroupBase(BaseModel):
    description: str
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
    user_id: int

    class Config:
        orm_mode = True


class WorkSchema(WorkGroupBase):
    id: int


class CreateWorkGroup(WorkGroupBase):
    pass

