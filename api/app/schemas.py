from datetime import datetime
from pydantic import BaseModel, root_validator


class HumanBase(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    phone: str

    class Config:
        orm_mode = True


class HumanSchema(HumanBase):
    id: int


class CreateHuman(HumanBase):
    pass


class ObjectBase(BaseModel):
    county: str
    region: str
    address: str
    object_type: str
    area: float
    photo: str
    active: bool

    class Config:
        orm_mode = True


class ObjectSchema(ObjectBase):
    id: int
    updated_at: datetime
    created_at: datetime
    owner: HumanSchema
    actual_user: HumanSchema


class CreateObject(ObjectBase):
    owner_id: int
    created_at: datetime

    class Config:
        validate_assignment = True

    @root_validator
    def update(cls, values):
        values["updated_at"] = datetime.utcnow()
        return values

    @root_validator
    def create(cls, values):
        values["created_at"] = datetime.utcnow()
        return values
