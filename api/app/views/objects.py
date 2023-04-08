from fastapi import APIRouter, Depends
from app import schemas
from app.service import objects as service
from core.engine import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post("")
async def create_object(
        object_: schemas.object.CreateObject,
        session: AsyncSession = Depends(get_async_session),
):
    return await service.create_object(object_, session)
