from pydantic import BaseModel

class TasksCreateSchema(BaseModel):
    title:str
    completed: bool

class TaskSchema(TasksCreateSchema):
    id:int