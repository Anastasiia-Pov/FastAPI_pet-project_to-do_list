from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import delete, select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from operations.models import operation
from operations.schemas import TaskCreate, TaskStatus, TaskImportance

router = APIRouter(
    tags=["Tasks"]
)


# получение всех задач
@router.get('/tasks')
async def get_all_tasks(user_id: int,
                        priority: TaskImportance = None,
                        status: TaskStatus = None,
                        session: AsyncSession = Depends(get_async_session)):
    try:
        if priority is not None and status is not None:
            query = select(operation).where(operation.c.user_id == user_id,
                                            operation.c.priority == priority,
                                            operation.c.status == status)
            result = await session.execute(query)
            return {'status': 'success',
                    'data': result.mappings().all(),
                    'details': None}
        elif priority is None and status is not None:
            query = select(operation).where(operation.c.user_id == user_id,
                                            operation.c.status == status)
            result = await session.execute(query)
            return {'status': 'success',
                    'data': result.mappings().all(),
                    'details': None}
        elif priority is not None and status is None:
            query = select(operation).where(operation.c.user_id == user_id,
                                            operation.c.priority == priority)
            result = await session.execute(query)
            return {'status': 'success',
                    'data': result.mappings().all(),
                    'details': None}
    except Exception:
        raise HTTPException(status_code=500,
                            detail={'status': 'error',
                                    'data': 'Error',
                                    'details': 'Что-то пошло не так'
                                    })


# получение задачи по id
@router.get('/task/{id}')
async def get_task_by_id(user_id: int,
                         id: int,
                         session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.user_id == user_id,
                                        operation.c.id == id)
        result = await session.execute(query)
        if result.scalars().first() == id:
            query = select(operation).where(operation.c.id == id)
            result = await session.execute(query)
            return {
                    'status': 'success',
                    'data': result.mappings().all(),
                    'details': None}
        else:
            return {'status': "No task with such a primary key."}
    except Exception:
        raise HTTPException(status_code=500,
                            detail={'status': 'error',
                                    'data': 'Error',
                                    'details': 'Что-то пошло не так'
                                    })


# добавление задачи
@router.post('/task')
async def add_task(new_task: TaskCreate,
                   session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(operation).values(**new_task.model_dump())
        await session.execute(stmt)
        await session.commit()
        return {'status': 'success'}
    except Exception:
        raise HTTPException(status_code=500,
                            detail={'status': 'error',
                                    'data': 'Error',
                                    'details': 'Что-то пошло не так'
                                    })


# редактирование задачи
@router.put('/task/{id}')
async def edit_task(id: int,
                    update_task: TaskCreate,
                    session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.id == id)
        result = await session.execute(query)
        # print(result.fetchone())
        if result.scalars().first() == id:
            stmt = (update(operation)
                    .where(operation.c.id == id)
                    .values(**update_task.model_dump()))
            await session.execute(stmt)
            await session.commit()
            return {'status': f'The decsription of the task-{id} is updated successfully'}
        else:
            return {'status': "No task with such a primary key."}
    except Exception:
        raise HTTPException(status_code=500,
                            detail={'status': 'error',
                                    'data': 'Error',
                                    'details': 'Что-то пошло не так'
                                    })


# удаление задачи по id:
@router.delete('/task/{id}')
async def delete_task(id: int,
                      session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = delete(operation).where(operation.c.id == id)
        await session.execute(stmt)
        await session.commit()
        return {'status': f'The task with id-{id} deleted successfully'}
    except Exception:
        return {'status': 'Something went wrong.'}
