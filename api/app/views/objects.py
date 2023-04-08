from fastapi import APIRouter, Depends
from app import schemas
from app.service import objects as service
from core.engine import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get("/")
async def create_object(session: AsyncSession = Depends(get_async_session)):
    return await service.get_objects_list(session)


@router.post("/")
async def create_object(
        object_: schemas.object.CreateObject,
        session: AsyncSession = Depends(get_async_session),
):
    return await service.create_object(object_, session)


@router.put("/")
async def update_object(
        pk: int,
        object_: schemas.object.UpdateObject,
        session: AsyncSession = Depends(get_async_session),
):
    return await service.update_object(pk, object_, session)


@router.delete("/")
async def update_object(
        pk: int,
        session: AsyncSession = Depends(get_async_session),
):
    return await service.delete_object(pk, session)
