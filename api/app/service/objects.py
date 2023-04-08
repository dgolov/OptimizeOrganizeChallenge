from typing import Any

from app import schemas
from core.repository_entity import ObjectEntity, TaskEntity, SolutionEntity


# Objects endpoints

async def get_objects_list(session, skip: int, limit: int) -> Any:
    return await ObjectEntity(session).get_objects_list(skip, limit)


async def create_object(object_: schemas.object.CreateObject, session) -> Any:
    return await ObjectEntity(session).create(data=object_)


async def update_object(pk: int, object_: schemas.object.CreateObject, session) -> Any:
    return await ObjectEntity(session).update(pk=pk, data=object_)


async def delete_object(pk: int, session) -> Any:
    return await ObjectEntity(session).delete(pk=pk)


async def create_object_from_xml(xml_str: str, session) -> Any:
    object_ = schemas.object.CreateObject.from_xml(xml_str)
    return await ObjectEntity(session).create(data=object_)


# Tasks endpoints

async def get_task_list(session) -> Any:
    return await TaskEntity(session).get_task_list()


async def create_task(object_: schemas.task.CreateTask, session) -> Any:
    return await TaskEntity(session).create(data=object_)


async def update_task(pk: int, object_: schemas.task.CreateTask, session) -> Any:
    return await TaskEntity(session).update(pk=pk, data=object_)


async def delete_task(pk: int, session) -> Any:
    return await TaskEntity(session).delete(pk=pk)


# Solutions endpoints

async def get_solution_list(session) -> Any:
    return await SolutionEntity(session).get_solution_list()


async def create_solution(object_: schemas.solution.CreateSolution, session) -> Any:
    return await SolutionEntity(session).create(data=object_)


async def update_solution(pk: int, object_: schemas.solution.CreateSolution, session) -> Any:
    return await SolutionEntity(session).update(pk=pk, data=object_)


async def delete_solution(pk: int, session) -> Any:
    return await SolutionEntity(session).delete(pk=pk)
