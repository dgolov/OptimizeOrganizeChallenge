from fastapi import APIRouter
from app import control


routes = APIRouter()

routes.include_router(
    control.router,
    prefix="/control",
)
