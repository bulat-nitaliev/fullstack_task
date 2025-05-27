from fastapi import FastAPI
from tasks.handler import router


app = FastAPI()

app.include_router(router)