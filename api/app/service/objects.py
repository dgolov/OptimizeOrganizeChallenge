from typing import Any

from app import schemas
from core.repository_entity import ObjectEntity


# Objects endpoints

async def get_objects_list(session, skip: int, limit: int) -> Any:
    return await ObjectEntity(session).get_objects_list(skip, limit)


async def get_objects_by_id(pk, session) -> Any:
    return await ObjectEntity(session).get_account_by_id(pk)


async def create_object(object_: schemas.object.CreateObject, session) -> Any:
    return await ObjectEntity(session).create(data=object_)


async def update_object(pk: int, object_: schemas.object.UpdateObject, session) -> Any:
    return await ObjectEntity(session).update(pk=pk, data=object_)


async def delete_object(pk: int, session) -> Any:
    return await ObjectEntity(session).delete(pk=pk)


async def create_object_from_xml(xml_str: str, session) -> Any:
    object_ = schemas.object.CreateObject.from_xml(xml_str)
    return await ObjectEntity(session).create(data=object_)
