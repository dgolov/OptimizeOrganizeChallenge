from fastapi_users import FastAPIUsers, fastapi_users
from app.users.auth import auth_backend
from app.models.user import User
from app.users.manager import get_user_manager


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()
