from fastapi import FastAPI
from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate, UserUpdate
from operations.router import router as router_operation

app = FastAPI(
    title="To-do List"
)

# AUTH
# login & logout
app.include_router(
    fastapi_users.get_auth_router(auth_backend,
                                  requires_verification=True ),
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
