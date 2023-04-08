from fastapi import APIRouter
from app import schemas
from app.service import objects as service

router = APIRouter()


@router.post("")
async def create_object(object_: schemas.object.CreateObject):
    return await service.create_object(object_)
