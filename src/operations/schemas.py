from datetime import datetime
from email.policy import default
from enum import StrEnum

from pydantic import BaseModel


class TaskCreate(BaseModel):
    task: str
    description: str
    priority: str
    status: str
    user_id: int


class TaskStatus(StrEnum):
    waiting = 'waiting'
    in_progress = 'in_progress'
    done = 'done'


class TaskImportance(StrEnum):
    low = 'low'
    middle = 'middle'
    high = 'high'
