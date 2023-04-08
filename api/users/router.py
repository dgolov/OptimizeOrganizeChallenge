
from fastapi import APIRouter

from .auth import auth_backend
from .schemas import UserRead, UserCreate, UserUpdate
from .utils import fastapi_users

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend, requires_verification=True),
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_verify_router(UserRead),
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_reset_password_router(),
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate, requires_verification=True),
    tags=["users"],
)
