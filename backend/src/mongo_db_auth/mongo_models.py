from typing import Optional
import uuid
from pydantic import BaseModel, Field
from datetime import datetime


class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    username: str
    email: str
    hashed_password: str
    registered_at: datetime.now
    super_user: bool = False
    verified: bool = False
    active: bool = True
