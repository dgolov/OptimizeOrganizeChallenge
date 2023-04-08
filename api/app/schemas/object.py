from datetime import datetime

from pydantic import BaseModel

from app.schemas.human import HumanSchema


class ConditionBase(BaseModel):
    value: str


class ConditionSchema(ConditionBase):
    id: int


class CreateCondition(ConditionBase):
    pass


class ObjectBase(BaseModel):
    county: str
    region: str
    address: str
    object_type: str
    area: float
    photo: str
    active: bool
    condition: ConditionSchema

    class Config:
        orm_mode = True


class ObjectSchema(ObjectBase):
    id: int
    updated_at: datetime
    created_at: datetime
    owner: HumanSchema
    actual_user: HumanSchema


class UpdateObject(ObjectBase):
    owner_id: int
    actual_user_id: int
    updated_at: datetime = datetime.utcnow()

    class Config:
        validate_assignment = True


class CreateObject(UpdateObject):
    created_at: datetime = datetime.utcnow()
