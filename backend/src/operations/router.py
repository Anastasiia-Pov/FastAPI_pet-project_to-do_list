from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import delete, select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import case
from database import get_async_session
from operations.models import operation
from operations.schemas import TaskCreate, TaskStatus, TaskImportance

router = APIRouter(
    tags=["Tasks"]
)


# получение всех задач
@router.get('/tasks', summary='Get all tasks')
async def get_tasks(user_id: int,
                    priority: TaskImportance = None,
                    status: TaskStatus = None,
                    session: AsyncSession = Depends(get_async_session),
                    ):
    """
    Get tasks according to the request:

    - **user_id**: whose tasks must be presented
    - **priority**: optional parameter
    - **status**: optional parameter
    """
    try:
        q = select(operation).where(operation.c.user_id == user_id)
        if (priority is not None):
            q = q.where(operation.c.priority == priority)
        if (status is not None):
            q = q.where(operation.c.status == status)
        result = await session.execute(q)
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
@router.get('/tasks/{id}', summary='Get task by id')
async def get_task_by_id(user_id: int,
                         id: int,
                         session: AsyncSession = Depends(get_async_session)):
    """
    Get task by user_id and id:

    - **user_id**: whose tasks must be presented
    - **id**: id of the task
    """
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
@router.post('/tasks', summary='Add new task')
async def add_task(new_task: TaskCreate,
                   session: AsyncSession = Depends(get_async_session)):
    """
    Create a task with all the information:

    - **task**: each task must have a name
    - **description**: optional description
    - **priority**: each task must have priority (low, middle, high)
    - **status**: each task must have status (waiting, in_progress, done)
    - **user_id**: each task must have a user_id (to whom a task belongs to)
    """
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
@router.put('/tasks/{id}', summary='Edit a task by id')
async def edit_task(id: int,
                    update_task: TaskCreate,
                    session: AsyncSession = Depends(get_async_session)):
    """
    Update a task with all the information:

    - **id**: id of the task
    - **task**: each task must have a name
    - **description**: optional description
    - **priority**: each task must have priority (low, middle, high)
    - **status**: each task must have status (waiting, in_progress, done)
    - **user_id**: each task must have a user_id (to whom a task belongs to)
    """
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


# частичное обновление задачи (изменение статуса или приоритета)
@router.patch('/tasks/{id}', summary='Edit status and priority of a task')
async def partial_edit(id: int,
                       priority: TaskImportance = TaskImportance.low,
                       status: TaskStatus = TaskStatus.in_progress,
                       session: AsyncSession = Depends(get_async_session)):
    """
    Partial update of a task:

    - **id**: id of a task
    - **priority**: default value 'low'
    - **status**: default value 'in_progress'
    """
    try:
        stmt = (update(operation)
                .where(operation.c.id == id)
                .values(status=status,
                        priority=priority))
        await session.execute(stmt)
        await session.commit()
        return {'status': f'The status & priority of the task-{id} is updated successfully'}
    except Exception:
        raise HTTPException(status_code=500,
                            detail={'status': 'error',
                                    'data': 'Error',
                                    'details': 'Что-то пошло не так'
                                    })


# удаление задачи по id:
@router.delete('/tasks/{id}', summary='Delete task by id')
async def delete_task(id: int,
                      session: AsyncSession = Depends(get_async_session)):
    """
    Delete a task by id:

    - **id**: id of a task
    """
    try:
        stmt = delete(operation).where(operation.c.id == id)
        await session.execute(stmt)
        await session.commit()
        return {'status': f'The task with id-{id} deleted successfully'}
    except Exception:
        return {'status': 'Something went wrong.'}
