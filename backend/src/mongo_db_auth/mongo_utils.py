from fastapi import Depends
from fastapi_users.db import BeanieBaseUser, BeanieUserDatabase

from mongo_db_auth.mongo_models import User


async def get_user_db():
    yield BeanieUserDatabase(User)
