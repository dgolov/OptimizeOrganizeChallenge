from pydantic import BaseModel
from datetime import datetime


class SolutionBase(BaseModel):
    description: str

    class Config:
        orm_mode = True


class SolutionSchema(SolutionBase):
    id: int
    created_at: datetime
    updated_at: datetime


class UpdateSolution(SolutionBase):
    updated_at: datetime = datetime.utcnow()

    class Config:
        validate_assignment = True


class CreateSolution(UpdateSolution):
    created_at: datetime = datetime.utcnow()

