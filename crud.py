

from sqlalchemy.orm import Session
from . import models, schemas

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Task).offset(skip).limit(limit).all()

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task: schemas.TaskCreate):
    db_task = get_task(db, task_id)
    if db_task:
        db_task.title = task.title
        db_task.description = task.description
        db_task.completed = task.completed
        db.commit()
        db.refresh(db_task)
        return db_task
    return None

def delete_task(db: Session, task_id: int):
    db_task = get_task(db, task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
        return {"message": "Task deleted successfully"}
    return {"error": "Task not found"}


