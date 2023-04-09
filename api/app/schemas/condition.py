from pydantic import BaseModel


class ConditionBase(BaseModel):
    value: str


class ConditionSchema(ConditionBase):
    id: int


class UpdateCondition(ConditionBase):
    ...


class CreateCondition(UpdateCondition):
    ...

