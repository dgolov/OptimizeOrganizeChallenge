from fastapi import APIRouter, Depends, UploadFile
from app import schemas
from app.service import objects as service
from core.engine import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get("/")
async def get_object(
        skip: int = schemas.basic.PAGINATION_SKIP,
        limit: int = schemas.basic.PAGINATION_LIMIT,
        session: AsyncSession = Depends(get_async_session)
):
    return await service.get_objects_list(session, skip=skip, limit=limit)


@router.post("/")
async def create_object(
        object_: schemas.object.CreateObject,
        session: AsyncSession = Depends(get_async_session),
):
    return await service.create_object(object_, session)


@router.put("/")
async def update_object(
        pk: int,
        object_: schemas.object.UpdateObject,
        session: AsyncSession = Depends(get_async_session),
):
    return await service.update_object(pk, object_, session)


@router.delete("/")
async def delete_object(
        pk: int,
        session: AsyncSession = Depends(get_async_session),
):
    return await service.delete_object(pk, session)


@router.post("/upload_xml")
async def upload_object(file: UploadFile,
                        session: AsyncSession = Depends(get_async_session),):
    contents = await file.read()
    return await service.create_object_from_xml(contents.decode(), session)
