from fastapi import APIRouter, Depends
from app import schemas
from app.service import solutions as service
from core.engine import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get("")
async def get_solutions_list(
        session: AsyncSession = Depends(get_async_session)
) -> list[schemas.solution.SolutionSchema]:
    return await service.get_solution_list(session)


@router.get("/{pk}")
async def get_solution_by_id(
        pk: int,
        session: AsyncSession = Depends(get_async_session)
) -> schemas.solution.SolutionSchema:
    return await service.get_solution_by_id(pk, session)


@router.post("")
async def create_solution(
        object_: schemas.solution.CreateSolution,
        session: AsyncSession = Depends(get_async_session),
) -> schemas.solution.SolutionSchema:
    return await service.create_solution(object_, session)


@router.put("/{pk}")
async def update_solution(
        pk: int,
        object_: schemas.solution.CreateSolution,
        session: AsyncSession = Depends(get_async_session),
) -> schemas.solution.SolutionSchema:
    return await service.update_solution(pk, object_, session)


@router.delete("/{pk}")
async def delete_solution(
        pk: int,
        session: AsyncSession = Depends(get_async_session),
):
    return await service.delete_solution(pk, session)
