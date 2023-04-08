from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    first_name: str
    middle_name: str
    last_name: str
    phone: str


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    middle_name: str
    last_name: str
    phone: str


class UserUpdate(schemas.BaseUserUpdate):
    first_name: str
    middle_name: str
    last_name: str
    phone: str
