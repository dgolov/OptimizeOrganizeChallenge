from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas
from core.engine import get_async_session
from app.service import work_groups as service

router = APIRouter()


@router.get("")
async def get_work_groups(session: AsyncSession = Depends(get_async_session)):
    return await service.get_work_group_list(session)


@router.post("")
async def create_work_group(
        object_: schemas.work_group.CreateWorkGroup,
        session: AsyncSession = Depends(get_async_session),
):
    return await service.create_work_group(object_, session)


@router.put("/{pk}")
async def update_work_group(
        pk: int,
        object_: schemas.work_group.CreateWorkGroup,
        session: AsyncSession = Depends(get_async_session),
):
    return await service.update_work_group(pk, object_, session)


@router.delete("/{pk}")
async def delete_work_group(
        pk: int,
        session: AsyncSession = Depends(get_async_session),
):
    return await service.delete_work_group(pk, session)


@router.get("/by_user/{user_id}")
async def get_work_groups_user(
        user_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    return await service.get_work_groups_user(user_id, session)
