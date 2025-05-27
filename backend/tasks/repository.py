from tasks.model import Tasks
from tasks.schemas import  TasksCreateSchema
from sqlalchemy.ext.asyncio import AsyncSession
from dataclasses import dataclass
from sqlalchemy import select, insert, delete
from .task_cache import TaskCache

@dataclass
class TaskRepository:
    db_session: AsyncSession

    async def get_tasks(self)->list[Tasks]:
        query = select(Tasks).order_by(Tasks.id.desc())
        async with self.db_session as session:
            res =  await session.execute(query)
            return res.scalars().all()
        

    async def add_task(
        self, task: TasksCreateSchema, task_cache: TaskCache, 
    ):

        query = (
            insert(Tasks)
            .values(**task.model_dump())
            .returning(Tasks.id)
        )
        async with self.db_session as session:
            task_id: int = await session.execute(query)
            await session.commit()
            await task_cache.drop_tasks()
            return task_id.scalar()
        
    async def get_task(self, task_id: int):
        async with self.db_session as session:
            return await session.get(Tasks, task_id)
        

    async def delete_task(self, task_id: int, task_cache: TaskCache):
        query = delete(Tasks).where(Tasks.id == task_id)
        async with self.db_session as session:
            await session.execute(query)
            await session.commit()
            await task_cache.drop_tasks()