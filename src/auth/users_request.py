from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import delete, select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from auth.models import User

router = APIRouter(
    prefix="/users_request",
    tags=["Users_request"]
)


@router.delete('/delete_user', tags=['Delete User'])
async def delete_user(user_id: int,
                      session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(User).where(User.c.id == user_id)
        result = await session.execute(query)
        if result.scalars().first() == user_id:
            query = select(User).where(operation.c.id == task_id)
            result = await session.execute(query)
            return {
                    'status': 'success',
                    'data': result.mappings().all(),
                    'details': None}
    except Exception:
        raise HTTPException(status_code=500,
                            detail={'status': 'error',
                                    'data': 'Error',
                                    'details': 'Что-то пошло не так'
                                    })