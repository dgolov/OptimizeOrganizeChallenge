from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey, Boolean, JSON
from sqlalchemy.orm import relationship

from core.engine import Base
from datetime import datetime


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    deadline = Column(DateTime)
    description = Column(String)
    responsible = Column(String)
    work_group_id = Column(Integer, ForeignKey("work_group.id"))
    solution_id = Column(Integer, ForeignKey("solution.id"))
    object_id = Column(Integer, ForeignKey("object.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    work_group = relationship("WorkGroup", back_populates="tasks")
    solution = relationship("Solution", back_populates="task")
    object = relationship("Object", back_populates="tasks")


class Object(Base):
    __tablename__ = "object"

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    county = Column(String)
    region = Column(String)
    address = Column(String)
    object_type = Column(String)
    area = Column(Float)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", lazy="joined", foreign_keys=[owner_id])
    actual_user_id = Column(Integer, ForeignKey("user.id"))
    actual_user = relationship("User", lazy="joined", foreign_keys=[actual_user_id])
    photo = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    active = Column(Boolean)
    extra_fields = Column(JSON)
    # coordinates = Column()
    tasks = relationship("Task", back_populates="object")
    condition_id = Column(Integer, ForeignKey("condition.id"))
    condition = relationship("Condition", lazy="joined", foreign_keys=[condition_id])


class Condition(Base):
    __tablename__ = "condition"

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    value = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)


class Solution(Base):
    __tablename__ = "solution"

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    # task_id = Column(Integer, ForeignKey("task.id"))
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    task = relationship("Task", back_populates="solution")


class WorkGroup(Base):
    __tablename__ = "work_group"

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    tasks = relationship("Task", back_populates="work_group")
    users = relationship('User', secondary='work_group_users', back_populates='work_groups')



class WorkGroupsUsers(Base):
    __tablename__ = "work_group_users"

    work_group_id = Column(Integer, ForeignKey('work_group.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)

    work_group = relationship('WorkGroup')
    user = relationship('User')




#
# class Role(Base):
#     __tablename__ = "role"
#
#     id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
#
#     """
#     - пользователь ГИН
#     - администратор рабочих групп
#     - исполнитель связанный с органами власти
#     - 3-4 органа исполнительной власти, иерархическая
#
#     """
