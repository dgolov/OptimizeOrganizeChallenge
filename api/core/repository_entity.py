from sqlalchemy import select, insert
from app.models.object import Object, Task, Solution, WorkGroup, Condition
from app.schemas.task import CreateTask
from app.schemas.solution import CreateSolution
from app.schemas.object import CreateObject, UpdateObject
from app.schemas.work_group import CreateWorkGroup
from app.schemas.condition import CreateCondition


class Base:
    def __init__(self, session):
        self.session = session

    @staticmethod
    async def _all(result):
        row = result.all()
        return [data[0] for data in row]

    @staticmethod
    def _first(result):
        result = result.first()
        if result:
            return result[0]
        else:
            return None

    @staticmethod
    def _one(result):
        return result.one()

    @staticmethod
    def _count(result):
        return len(result)

    async def _add(self, obj, data):
        instance = obj(**data.dict())
        self.session.add(instance)
        await self.session.commit()
        return instance

    async def _update(self, obj, data):
        for field, value in data.dict(exclude_none=True).items():
            setattr(obj, field, value)
        await self.session.commit()
        return obj

    async def _delete(self, obj):
        await self.session.delete(obj)
        await self.session.commit()
        return {
            "status": "success"
        }


class ObjectEntity(Base):
    async def get_objects_list(self, skip: int, limit: int):
        query = select(Object).filter(Object.active == True)
        # TODO Не работает :)
        # query = select(Object).filter(Object.active == True).skip(skip).limit(limit)
        query_result = await self.session.execute(query)
        return await self._all(query_result)

    async def create(self, data: CreateObject):
        return await self._add(obj=Object, data=data)

    async def update(self, pk: int, data: UpdateObject):
        item = await self.session.get(Object, pk)
        return await self._update(item, data)

    async def delete(self, pk: int):
        item = await self.session.get(Object, pk)
        return await self._delete(item)

    async def get_account_by_id(self, pk: int):
        query = select(Object).filter(Object.id == int(pk))
        result = await self.session.execute(query)
        return self._first(result)


class TaskEntity(Base):
    async def get_task_list(self):
        query = select(Task)
        query_result = await self.session.execute(query)
        return await self._all(query_result)

    async def create(self, data: CreateTask):
        return await self._add(obj=Task, data=data)

    async def update(self, pk: int, data: CreateTask):
        task = await self.session.get(Task, pk)
        return await self._update(task, data)

    async def delete(self, pk: int):
        task = await self.session.get(Task, pk)
        return await self._delete(task)

    async def get_task_by_id(self, pk: int):
        query = select(Task).filter(Task.id == int(pk))
        result = await self.session.execute(query)
        return self._first(result)


class SolutionEntity(Base):
    async def get_solution_list(self):
        query = select(Solution)
        query_result = await self.session.execute(query)
        return await self._all(query_result)

    async def create(self, data: CreateSolution):
        return await self._add(obj=Solution, data=data)

    async def update(self, pk: int, data: CreateSolution):
        solution = await self.session.get(Solution, pk)
        return await self._update(solution, data)

    async def delete(self, pk: int):
        solution = await self.session.get(Solution, pk)
        return await self._delete(solution)

    async def get_solution_by_id(self, pk: int):
        query = select(Solution).filter(Solution.id == int(pk))
        result = await self.session.execute(query)
        return self._first(result)


class WorkGroupEntity(Base):
    async def get_work_group_list(self):
        query = select(WorkGroup)
        query_result = await self.session.execute(query)
        return await self._all(query_result)

    async def create(self, data: CreateWorkGroup):
        return await self._add(obj=WorkGroup, data=data)

    async def update(self, pk: int, data: CreateWorkGroup):
        work_group = await self.session.get(WorkGroup, pk)
        return await self._update(work_group, data)

    async def delete(self, pk: int):
        work_group = await self.session.get(WorkGroup, pk)
        return await self._delete(work_group)

    async def get_works_group_by_user_id(self, pk: int):
        query = select(WorkGroup).filter(WorkGroup.user_id == int(pk))
        result = await self.session.execute(query)
        return self._first(result)


class ConditionEntity(Base):
    async def get_condition_list(self):
        query = select(Condition)
        query_result = await self.session.execute(query)
        return await self._all(query_result)

    async def create(self, data: CreateCondition):
        return await self._add(obj=Condition, data=data)

    async def update(self, pk: int, data: CreateCondition):
        condition = await self.session.get(Condition, pk)
        return await self._update(condition, data)

    async def delete(self, pk: int):
        condition = await self.session.get(Condition, pk)
        return await self._delete(condition)

    async def get_condition_by_id(self, pk: int):
        query = select(Condition).filter(Condition.id == int(pk))
        result = await self.session.execute(query)
        return self._first(result)
