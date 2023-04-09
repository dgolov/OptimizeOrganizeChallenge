from typing import Any

from app import schemas
from core.repository_entity import ConditionEntity


# Conditions endpoints

async def get_condition_list(session) -> Any:
    return await ConditionEntity(session).get_condition_list()


async def get_condition_by_id(pk, session) -> Any:
    return await ConditionEntity(session).get_condition_by_id(pk)


async def create_condition(object_: schemas.condition.CreateCondition, session) -> Any:
    return await ConditionEntity(session).create(data=object_)


async def update_condition(pk: int, object_: schemas.condition.CreateCondition, session) -> Any:
    return await ConditionEntity(session).update(pk=pk, data=object_)


async def delete_condition(pk: int, session) -> Any:
    return await ConditionEntity(session).delete(pk=pk)

