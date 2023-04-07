from fastapi_users import FastAPIUsers, fastapi_users
from users.auth import auth_backend
from users.models import User
from users.manager import get_user_manager


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()
