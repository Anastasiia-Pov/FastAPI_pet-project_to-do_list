import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth.base_config import auth_backend, fastapi_users
from mongo_db_auth.mongo_schemas import UserRead, UserCreate, UserUpdate
# from operations.router import router as router_operation
from contextlib import asynccontextmanager
# from database import create_tables, shut_down_db
from pages.router import router as router_pages

from pymongo import AsyncMongoClient
from config import MONGO_DB, MONGO_HOST, MONGO_PORT
from mongo_db_operations.router import router_mongo
import motor.motor_asyncio
from beanie import init_beanie
from mongo_db_auth.mongo_models import User
from database_mng import db
from mongo_db_operations.mongodb_task_models import TaskCreate, UpdateTask


log = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # app.mongodb_client = motor.motor_asyncio.AsyncIOMotorClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/", uuidRepresentation="standard")
    # app.database = app.mongodb_client[MONGO_DB]
    await init_beanie(database=db,
                      document_models=[User, TaskCreate, UpdateTask, ],)
    # col_tasks = app.database["tasks"]
    # col_users = app.database["users"]
    log.warning("Connected to the MongoDB database!")
    yield
    await app.mongodb_client.close()
    log.warning("Disconnected from the MongoDB database!")


app = FastAPI(
    lifespan=lifespan,
    title="To-do List",
)

# app.include_router(router_operation)
app.include_router(router_mongo)
app.include_router(router_pages)


origins = [
    "http://localhost",
    "http://localhost:5173",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie",
                   "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin",
                   "Authorization"],
)


# AUTH
# login & logout
# app.include_router(
#     fastapi_users.get_auth_router(auth_backend,
#                                   requires_verification=True),
#     prefix="/auth/jwt",
#     tags=["Auth-login&logout"],
# )

# # register
# app.include_router(
#     fastapi_users.get_register_router(UserRead, UserCreate),
#     prefix="/auth",
#     tags=["Auth-register"],
# )

# verification
# app.include_router(
#     fastapi_users.get_verify_router(UserRead),
#     prefix="/auth",
#     tags=["Auth-verification"],
# )

# # forgot&reset password
# app.include_router(
#     fastapi_users.get_reset_password_router(),
#     prefix="/auth",
#     tags=["Auth-forgot&reset password"],
# )


# # USERS
# app.include_router(
#     fastapi_users.get_users_router(UserRead,
#                                    UserUpdate),
#     prefix="/users",
#     tags=["Users"],
# )
