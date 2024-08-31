from typing import Annotated, Dict

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd, STask

router = APIRouter(prefix="/tasks", tags=["Таски"])


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks


@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]):
    task_id = await TaskRepository.add_one(task)

    return {"ok": True, "task_id": task_id}
