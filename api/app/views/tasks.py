from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas
from app.service import tasks as service

from core.engine import get_async_session

router = APIRouter()


@router.get("")
async def get_tasks_list(
        session: AsyncSession = Depends(get_async_session)
) -> list[schemas.task.TaskSchema]:
    return await service.get_task_list(session)


@router.get("/{pk}")
async def get_task_by_id(
        pk: int,
        session: AsyncSession = Depends(get_async_session)
) -> schemas.task.TaskSchema:
    return await service.get_task_by_id(pk, session)


@router.post("")
async def create_task(
        object_: schemas.task.CreateTask,
        session: AsyncSession = Depends(get_async_session),
) -> schemas.task.TaskSchema:
    return await service.create_task(object_, session)


@router.put("/{pk}")
async def update_task(
        pk: int,
        object_: schemas.task.CreateTask,
        session: AsyncSession = Depends(get_async_session),
) -> schemas.task.TaskSchema:
    return await service.update_task(pk, object_, session)


@router.delete("/{pk}")
async def delete_task(
        pk: int,
        session: AsyncSession = Depends(get_async_session),
):
    return await service.delete_task(pk, session)
