from fastapi import APIRouter, HTTPException

from app.schemas import TaskCreate, TaskResponse
from app.services import task_service


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate):
    return task_service.create_task(task)


@router.get("", response_model=list[TaskResponse])
def get_tasks(completed: bool | None = None):
    return task_service.get_tasks_by_completed(completed)


@router.get("/{task_id}", response_model=TaskResponse)
def get_task_by_id(task_id: int):
    task = task_service.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, new_task: TaskCreate):
    task = task_service.update_task(task_id, new_task)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.delete("/{task_id}")
def delete_task(task_id: int):
    success = task_service.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}
