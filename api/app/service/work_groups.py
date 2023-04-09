from typing import Any

from app import schemas
from core.repository_entity import WorkGroupEntity


async def get_work_group_list(session) -> Any:
    return await WorkGroupEntity(session).get_work_group_list()


async def create_work_group(object_: schemas.work_group.CreateWorkGroup, session) -> Any:
    return await WorkGroupEntity(session).create(data=object_)


async def update_work_group(pk: int, object_: schemas.work_group.CreateWorkGroup, session) -> Any:
    return await WorkGroupEntity(session).update(pk=pk, data=object_)


async def delete_work_group(pk: int, session) -> Any:
    return await WorkGroupEntity(session).delete(pk=pk)


async def get_work_groups_user(user_id: int, session) -> Any:
    return await WorkGroupEntity(session).get_works_group_by_user_id(user_id)
