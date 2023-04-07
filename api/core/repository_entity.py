from sqlalchemy import select, insert
from api.app.models import Object, Human
from api.app.schemas import CreateObject, CreateHuman


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
    async def get_account_list(self):
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