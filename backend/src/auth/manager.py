import logging
from typing import Optional, Union

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin, InvalidPasswordException, exceptions, models, schemas

from auth.models import User
from auth.schemas import UserCreate
from auth.utils import get_user_db

from config import SECRET_VERIF, SECRET_RESET

log = logging.getLogger(__name__)

class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET_RESET
    verification_token_secret = SECRET_VERIF

    async def validate_password(
        self,
        password: str,
        user: Union[UserCreate, User],
    ) -> None:
        if len(password) < 8:
            raise InvalidPasswordException(
                reason="Password should be at least 8 characters"
            )
        if user.email in password:
            raise InvalidPasswordException(
                reason="Password should not contain e-mail"
            )

    # регистрация пользователя
    async def on_after_register(self,
                                user: User,
                                request: Optional[Request] = None):
        # print(f"User {user.id} has registered.")
        log.warning("User %r has registered.", user.id)

    # запрос на сброс пароля пользователем
    async def on_after_forgot_password(self,
                                       user: User,
                                       token: str,
                                       request: Optional[Request] = None):
        # print(f"User {user.id} has forgot their password. Reset token: {token}")
        log.warning("User %r has forgot their password.\nReset token: %r",
                    user.id, token)

    # запрос верификации пользотвателем
    async def on_after_request_verify(self,
                                      user: User,
                                      token: str,
                                      request: Optional[Request] = None):
        log.warning("""Verification requested for user %r.
Verification token: %r""", user.id, token)

    async def on_before_delete(self,
                               user: User,
                               request: Optional[Request] = None):
        log.warning("User %r is going to be deleted.", user.id)

    async def on_after_delete(self,
                              user: User,
                              request: Optional[Request] = None):
        log.warning("User %r is successfully deleted", user.id)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
