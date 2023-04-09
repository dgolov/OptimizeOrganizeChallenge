from typing import Any

from app import schemas
from core.repository_entity import TaskEntity


# Tasks endpoints

async def get_task_list(session) -> Any:
    return await TaskEntity(session).get_task_list()


async def get_task_by_id(pk, session) -> Any:
    return await TaskEntity(session).get_task_by_id(pk)


async def create_task(object_: schemas.task.CreateTask, session) -> Any:
    return await TaskEntity(session).create(data=object_)


async def update_task(pk: int, object_: schemas.task.CreateTask, session) -> Any:
    return await TaskEntity(session).update(pk=pk, data=object_)


async def delete_task(pk: int, session) -> Any:
    return await TaskEntity(session).delete(pk=pk)

