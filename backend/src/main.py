import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate, UserUpdate
from operations.router import router as router_operation
from contextlib import asynccontextmanager

from database import create_tables, shut_down_db
log = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    log.warning("БД готова")
    yield
    log.warning("БД остановлена")

app = FastAPI(
    lifespan=lifespan,
    title="To-do List",
)


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
app.include_router(
    fastapi_users.get_auth_router(auth_backend,
                                  requires_verification=True),
    prefix="/auth/jwt",
    tags=["Auth-login&logout"],
)

# register
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth-register"],
)

# verification
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["Auth-verification"],
)

# forgot&reset password
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["Auth-forgot&reset password"],
)


# USERS
app.include_router(
    fastapi_users.get_users_router(UserRead,
                                   UserUpdate),
    prefix="/users",
    tags=["Users"],
)


app.include_router(router_operation)
