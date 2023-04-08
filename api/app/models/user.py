from core.engine import Base, get_async_session
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.ext.asyncio import AsyncSession


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    email: str = Column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
