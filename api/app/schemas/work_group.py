from pydantic import BaseModel
from datetime import datetime


class WorkGroupBase(BaseModel):
    id: int
    description: str
    created_at: datetime
    updated_at: datetime
    user_id: int


class CreateWorkGroup(WorkGroupBase):
    pass

