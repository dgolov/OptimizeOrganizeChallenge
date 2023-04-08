from pydantic import BaseModel
from datetime import datetime


class SolutionBase(BaseModel):
    id: int
    description: str
    created_at: datetime
    updated_at: datetime


class CreateSolution(SolutionBase):
    pass

