
from tasks import TaskService, TaskRepository, TaskCache
from fastapi import Depends
from infrastructure import helper, get_connect

from sqlalchemy.ext.asyncio import AsyncSession


async def get_db_session():
    async with helper.session_factory() as session:
        yield session


async def get_task_repository(db_session: AsyncSession = Depends(get_db_session)):
    return TaskRepository(db_session=db_session)


def get_task_cache_repository() -> TaskCache:
    redis_connect = get_connect()
    return TaskCache(redis_connect)


def get_task_servise(
    task_repo: TaskRepository = Depends(get_task_repository),
    task_cache: TaskCache = Depends(get_task_cache_repository),
) -> TaskService:
    return TaskService(task_repo=task_repo, task_cache=task_cache)

