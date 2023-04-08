from fastapi import APIRouter
from .users import router as users_router
from .objects import router as objects_router

router = APIRouter()

router.include_router(prefix="/users", router=users_router, tags=["Users"])
router.include_router(prefix="/objects", router=objects_router, tags=["Objects"])
