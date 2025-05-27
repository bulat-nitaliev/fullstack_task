from dataclasses import dataclass
from tasks.repository import TaskCache, TaskRepository
from tasks.schemas import TaskSchema, TasksCreateSchema
from infrastructure.exception import TaskNotFoundException


@dataclass
class TaskService:
    task_repo: TaskRepository
    task_cache: TaskCache

    async def get_tasks(self):

        if task_cache_repo := await self.task_cache.get_tasks():
            print(task_cache_repo, "cache_______")
            return task_cache_repo

        tasks = await self.task_repo.get_tasks()
        tasks_shema = [TaskSchema.model_validate(task.__dict__) for task in tasks]
        if tasks_shema:
            await self.task_cache.set_tasks(tasks_shema)
        return tasks_shema


    async def create_task(self, body: TasksCreateSchema) -> TaskSchema:
        task_id = await self.task_repo.add_task(
            task=body, task_cache=self.task_cache,
        )

        task = await self.task_repo.get_task(task_id=task_id)
        return TaskSchema(
            title=task.title, 
            id=task.id, 
            completed=task.completed
            )
    
    async def delete_task(self, task_id: int):
        task = await self.task_repo.get_task(task_id=task_id)
        if not task:
            raise TaskNotFoundException
        await self.task_repo.delete_task(task_id=task_id, task_cache=self.task_cache)

