from fastapi import APIRouter, Depends
from app import schemas
from app.service import conditions as service
from core.engine import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get("")
async def get_conditions_list(session: AsyncSession = Depends(get_async_session)):
    return await service.get_condition_list(session)


@router.get("/{pk}")
async def get_condition_by_id(pk: int, session: AsyncSession = Depends(get_async_session)):
    return await service.get_condition_by_id(pk, session)


@router.post("")
async def create_condition(
        object_: schemas.condition.CreateCondition,
        session: AsyncSession = Depends(get_async_session),
):
    return await service.create_condition(object_, session)


@router.put("/{pk}")
async def update_condition(
        pk: int,
        object_: schemas.condition.CreateCondition,
        session: AsyncSession = Depends(get_async_session),
):
    return await service.update_condition(pk, object_, session)


@router.delete("/{pk}")
async def delete_condition(
        pk: int,
        session: AsyncSession = Depends(get_async_session),
):
    return await service.delete_condition(pk, session)
