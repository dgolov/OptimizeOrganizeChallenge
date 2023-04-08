from pydantic import BaseModel


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
