from redis import asyncio as Redis
from typing import List
from tasks.schemas import TaskSchema
from dataclasses import dataclass

import json

@dataclass
class TaskCache:
    redis: Redis

    async def get_tasks(self) -> List[TaskSchema]:
        async with self.redis as redis:
            tasks = await redis.lrange("tasks", 0, -1)
            
            if tasks:
                return [TaskSchema.model_validate(json.loads(task)) for task in tasks]
            return []

    async def set_tasks(self, tasks: List[TaskSchema]):
        task_json = [task.model_dump_json() for task in tasks]
        async with self.redis as redis:
            await redis.expire("tasks", 60)
            await redis.lpush("tasks", *task_json)

    async def drop_tasks(self):
        async with self.redis as redis:
            await redis.delete("tasks")
