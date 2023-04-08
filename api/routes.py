from fastapi import APIRouter
from app import control
from users import router as auth


routes = APIRouter()

routes.include_router(
    control.router,
    prefix="/control",
)

routes.include_router(
    auth.router,
    prefix="/auth",
)
