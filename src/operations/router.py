from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import delete, select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from operations.models import operation
from operations.schemas import TaskCreate, TaskStatus, TaskImportance

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


# получение всех задач
@router.get('/get_all', tags=['get all tasks'])
async def get_all_tasks(user_id: int,
                        session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.user_id == user_id)
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


# получение задачи по id
@router.get('/get_by_id', tags=['get task by id'])
async def get_task_by_id(user_id: int,
                         task_id: int,
                         session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.user_id == user_id,
                                        operation.c.id == task_id)
        result = await session.execute(query)
        if result.scalars().first() == task_id:
            query = select(operation).where(operation.c.id == task_id)
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


# получение задачи - по приоритету:
@router.get("/get_by_priority", tags=['get task by priority'])
async def get_task_priority(user_id: int,
                            type: TaskImportance,
                            session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.user_id == user_id,
                                        operation.c.priority == type)
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


# получение задачи - по готовности:
@router.get("/get_by_status", tags=['get task by status'])
async def get_task_status(user_id: int,
                          type: TaskStatus,
                          session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.user_id == user_id,
                                        operation.c.status == type)
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


# получение задачи - по статусу и готовности:
@router.get("/get_by_status_and_priority",
            tags=['get tasks by status and priority'])
async def get_task_pr_st(user_id: int,
                         priority: TaskImportance,
                         status: TaskStatus,
                         session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.user_id == user_id,
                                        operation.c.status == status,
                                        operation.c.priority == priority)
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


# добавление задачи
@router.post('/add_task', tags=['add task'])
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
@router.put('/update_task', tags=['update task by id'])
async def edit_task(task_id: int,
                    update_task: TaskCreate,
                    session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.id == task_id)
        result = await session.execute(query)
        # print(result.fetchone())
        if result.scalars().first() == task_id:
            stmt = (update(operation)
                    .where(operation.c.id == task_id)
                    .values(**update_task.model_dump()))
            await session.execute(stmt)
            await session.commit()
            return {'status': f'The decsription of the task-{task_id} is updated successfully'}
        else:
            return {'status': "No task with such a primary key."}
    except Exception:
        raise HTTPException(status_code=500,
                            detail={'status': 'error',
                                    'data': 'Error',
                                    'details': 'Что-то пошло не так'
                                    })


# удаление задачи по id:
@router.delete('/delete_task', tags=['delete task by id'])
async def delete_task(task_id: int,
                      session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = delete(operation).where(operation.c.id == task_id)
        await session.execute(stmt)
        await session.commit()
        return {'status': f'The task with id-{task_id} deleted successfully'}
    except Exception:
        return {'status': 'Something went wrong.'}
