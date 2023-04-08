from sqlalchemy import select, insert
from app.models.human import Human
from app.models.object import Object, Task, Solution, WorkGroup
from app.schemas.human import CreateHuman
from app.schemas.task import CreateTask
from app.schemas.solution import CreateSolution
from app.schemas.object import CreateObject


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
        data = data.dict()
        query = insert(obj).values(**data)
        await self.session.execute(query)
        await self.session.commit()
        return {
            "status": "success"
        }

    async def _update(self, obj, data):
        for field, value in data.dict().items():
            setattr(obj, field, value)
        await self.session.commit()
        return {
            "status": "success"
        }

    async def _delete(self, obj):
        await self.session.delete(obj)
        await self.session.commit()
        return {
            "status": "success"
        }


class ObjectEntity(Base):
    async def get_objects_list(self):
        query = select(Object)
        query_result = await self.session.execute(query)
        return await self._all(query_result)

    async def create(self, data: CreateObject):
        return await self._add(obj=Object, data=data)

    async def update(self, pk: int, data: CreateObject):
        item = await self.session.get(Object, pk)
        return await self._update(item, data)

    async def delete(self, pk: int):
        item = await self.session.get(Object, pk)
        return await self._delete(item)

    async def get_account_by_id(self, pk: int):
        query = select(Object).filter(Object.id == int(pk))
        result = await self.session.execute(query)
        return self._first(result)


class HumanEntity(Base):
    async def get_human_list(self):
        query = select(Human)
        query_result = await self.session.execute(query)
        return await self._all(query_result)

    async def create(self, data: CreateHuman):
        return await self._add(obj=Object, data=data)

    async def update(self, pk: int, data: CreateHuman):
        human = await self.session.get(Human, pk)
        return await self._update(human, data)

    async def delete(self, pk: int):
        human = await self.session.get(Human, pk)
        return await self._delete(human)

    async def get_account_by_id(self, pk: int):
        query = select(Human).filter(Human.id == int(pk))
        result = await self.session.execute(query)
        return self._first(result)


class TaskEntity(Base):
    async def get_task_list(self):
        query = select(Task)
        query_result = await self.session.execute(query)
        return await self._all(query_result)

    async def create(self, data: CreateTask):
        return await self._add(obj=Object, data=data)

    async def update(self, pk: int, data: CreateTask):
        task = await self.session.get(Task, pk)
        return await self._update(task, data)

    async def delete(self, pk: int):
        task = await self.session.get(Task, pk)
        return await self._delete(task)


class SolutionEntity(Base):
    async def get_task_list(self):
        query = select(Solution)
        query_result = await self.session.execute(query)
        return await self._all(query_result)

    async def create(self, data: CreateSolution):
        return await self._add(obj=Object, data=data)

    async def update(self, pk: int, data: CreateSolution):
        solution = await self.session.get(Solution, pk)
        return await self._update(solution, data)

    async def delete(self, pk: int):
        solution = await self.session.get(Solution, pk)
        return await self._delete(solution)


class WorkGroupEntity(Base):
    pass



