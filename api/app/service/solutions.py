from typing import Any

from app import schemas
from core.repository_entity import SolutionEntity


# Solutions endpoints

async def get_solution_list(session) -> Any:
    return await SolutionEntity(session).get_solution_list()


async def get_solution_by_id(pk, session) -> Any:
    return await SolutionEntity(session).get_solution_by_id(pk)


async def create_solution(object_: schemas.solution.CreateSolution, session) -> Any:
    return await SolutionEntity(session).create(data=object_)


async def update_solution(pk: int, object_: schemas.solution.CreateSolution, session) -> Any:
    return await SolutionEntity(session).update(pk=pk, data=object_)


async def delete_solution(pk: int, session) -> Any:
    return await SolutionEntity(session).delete(pk=pk)

