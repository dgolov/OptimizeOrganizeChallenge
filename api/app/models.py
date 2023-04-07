from api.core.engine import Base
from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class Object(Base):
    __tablename__ = "object"

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    county = Column(String)
    region = Column(String)
    address = Column(String)
    object_type = Column(String)
    area = Column(Float)
    owner_id = Column(Integer, ForeignKey('human.id'))
    owner = relationship("Human", lazy="joined")
    actual_user_id = Column(Integer, ForeignKey('human.id'))
    actual_user = relationship("Human", lazy="joined")
    photo = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    active = Column(Boolean)


class Human(Base):
    __tablename__ = "human"

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    phone = Column(String)
