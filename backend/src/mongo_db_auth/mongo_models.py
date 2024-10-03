import uuid
from pydantic import Field
from datetime import datetime
import motor.motor_asyncio
from beanie import Document
from fastapi_users.db import BeanieBaseUser


class User(Document):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    username: str
    email: str
    hashed_password: str
    registered_at: datetime.now
    super_user: bool = False
    verified: bool = False
    active: bool = True
