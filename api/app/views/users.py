from fastapi import APIRouter
from app import schemas
from app.service import users as service
from app.users.auth import auth_backend
from app.schemas.user import UserRead, UserCreate, UserUpdate
from app.users.utils import fastapi_users


router = APIRouter()


@router.get("")
async def get_users(skip: int = schemas.basic.PAGINATION_SKIP,
                    limit: int = schemas.basic.PAGINATION_LIMIT):
    await service.get_users(skip, limit)


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

