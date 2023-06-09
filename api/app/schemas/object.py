from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel

from app.schemas.user import UserRead
from app.schemas.condition import ConditionSchema

from app.utils import parse_xml


class ObjectBase(BaseModel):
    county: str
    region: str
    address: str
    object_type: str
    area: float
    photo: str = ""
    active: bool = True
    extra_fields: dict[str, Any] = {}

    class Config:
        orm_mode = True


class ObjectSchema(ObjectBase):
    id: int
    updated_at: datetime
    created_at: datetime
    owner: UserRead
    actual_user: UserRead
    condition: ConditionSchema


class UpdateObject(ObjectBase):
    owner_id: Optional[int]
    actual_user_id: Optional[int]
    condition_id: Optional[int]
    updated_at: datetime = datetime.utcnow()

    class Config:
        validate_assignment = True


class CreateObject(UpdateObject):
    created_at: datetime = datetime.utcnow()

    @classmethod
    def from_xml(cls, xml_string: str) -> "CreateObject":
        if not bool(xml_dict := parse_xml(xml_string)):
            raise ValueError("Invalid XML")
        data = {}
        for key, value in xml_dict.items():
            if key in cls.__fields__:
                data[key] = value
                continue
            data.setdefault("extra_fields", {})
            data["extra_fields"][key] = value
        return cls.parse_obj(data)
