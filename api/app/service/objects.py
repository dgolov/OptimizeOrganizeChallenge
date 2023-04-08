from typing import Any

from app import schemas
from core.repository_entity import ObjectEntity


async def create_object(object_: schemas.object.CreateObject, session) -> Any:
    object_entity = ObjectEntity(session)
    return await object_entity.create(data=object_)
