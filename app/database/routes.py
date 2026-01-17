from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import get_db
from app import models

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/")
def create_task(title: str, description: str = "", db: Session = Depends(get_db)):
    task = models.Task(title=title, description=description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.get("/")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()


@router.get("/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return {"message": "Task deleted"}
