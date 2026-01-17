from fastapi import FastAPI

from app.database.db import engine
from app import models
from app.database.routes import router as task_router

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

app.include_router(task_router)


@app.get("/")
def root():
    return {"status": "API is running"}
