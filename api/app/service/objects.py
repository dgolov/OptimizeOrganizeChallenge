from typing import Any

from app import schemas
from core.repository_entity import ObjectEntity


async def get_objects_list(session) -> Any:
    print(123)
    return await ObjectEntity(session).get_objects_list()


async def create_object(object_: schemas.object.CreateObject, session) -> Any:
    return await ObjectEntity(session).create(data=object_)


async def update_object(pk: int, object_: schemas.object.CreateObject, session) -> Any:
    return await ObjectEntity(session).update(pk=pk, data=object_)
