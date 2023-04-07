from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


@router.get("/")
async def test() -> dict:
    return {"test": "Ok"}


class UserCreate(BaseModel):
    name: str
    password: str


@router.post("/")
async def create_human(user: UserCreate) -> dict:
    return {"test": "Ok"}
