from pydantic import BaseModel


class ConditionBase(BaseModel):
    value: str

    class Config:
        orm_mode = True


class ConditionSchema(ConditionBase):
    id: int


class CreateCondition(ConditionBase):
    ...


class UpdateCondition(ConditionBase):
    ...
