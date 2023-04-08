from fastapi import APIRouter
from app import schemas
from app.service import users as service


router = APIRouter()


@router.get("")
async def get_users(skip: int = schemas.basic.PAGINATION_SKIP,
                    limit: int = schemas.basic.PAGINATION_LIMIT):
    await service.get_users(skip, limit)
