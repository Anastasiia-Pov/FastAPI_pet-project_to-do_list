from enum import StrEnum
from typing import Optional
import uuid
from pydantic import BaseModel, Field


class TaskStatus(StrEnum):
    waiting = 'waiting'
    in_progress = 'in_progress'
    done = 'done'


class TaskPriority(StrEnum):
    low = 'low'
    middle = 'middle'
    high = 'high'


class TaskCreate(BaseModel):
    task: str
    description: str
    priority: TaskPriority
    status: TaskStatus
    username: str


class UpdateTask(BaseModel):
    task: str
    description: str
    priority: TaskPriority
    status: TaskStatus
