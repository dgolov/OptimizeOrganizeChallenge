from sqlalchemy import Column, String, Integer

from core.engine import Base


class Human(Base):
    __tablename__ = "human"

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    phone = Column(String)
