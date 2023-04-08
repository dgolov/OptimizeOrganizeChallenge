from datetime import datetime
from typing import Any

from pydantic import BaseModel, ValidationError

from app.schemas.human import HumanSchema
from app.utils import parse_xml


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
    extra_fields: dict[str, Any]

    class Config:
        orm_mode = True


class ObjectSchema(ObjectBase):
    id: int
    updated_at: datetime
    created_at: datetime
    owner: HumanSchema
    actual_user: HumanSchema
    condition: ConditionSchema


class UpdateObject(ObjectBase):
    owner_id: int
    actual_user_id: int
    condition_id: int
    updated_at: datetime = datetime.utcnow()

    class Config:
        validate_assignment = True


class CreateObject(UpdateObject):
    created_at: datetime = datetime.utcnow()

    @classmethod
    def from_xml(cls, xml_string: str) -> "CreateObject":
        if not bool(xml_dict := parse_xml(xml_string)):
            raise ValidationError("Invalid xml")
        data = {}
        for key, value in xml_dict.items():
            if key in cls.__fields__:
                data[key] = value
                continue
            data.setdefault("extra_fields", {})
            data["extra_fields"][key] = value
        return cls.parse_obj(data)


