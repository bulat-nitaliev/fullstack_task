from fastapi import APIRouter, Depends, status, HTTPException
from tasks.schemas import TaskSchema, TasksCreateSchema
from typing import List, Annotated
from tasks.service import TaskService
from dependecy import  get_task_servise
from infrastructure.exception import TaskNotFoundException


router = APIRouter(tags=["tasks"], prefix="/api")


@router.post("/tasks", response_model=TaskSchema)
async def create_task(
    body: TasksCreateSchema,
    task_service: Annotated[TaskService, Depends(get_task_servise)],
):
    return await task_service.create_task(body=body)


@router.get("/tasks", response_model=List[TaskSchema])
async def get_task(
    task_service: TaskService = Depends(get_task_servise),
):
    return await task_service.get_tasks()
    

@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def destroy_task(
    task_id: int,
    task_service: Annotated[TaskService, Depends(get_task_servise)]
):
    try:
        await task_service.delete_task(task_id=task_id)
    except TaskNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.detail)