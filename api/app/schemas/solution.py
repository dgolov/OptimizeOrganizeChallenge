from pydantic import BaseModel
from datetime import datetime


class SolutionBase(BaseModel):
    description: str
    created_at: datetime
    updated_at: datetime


class SolutionSchema(SolutionBase):
    id: int


class CreateSolution(SolutionBase):
    pass

