# FastAPI_pet-project_to-do_list

Project is motivated by learning backend using FastAPI framework, PostgreSQL, SQLAlchemy and PyTest.

Project structure:
#### Backend
```
backend/
├─ src/
│  ├─ auth/
│  │  ├─ base_config.py
│  │  ├─ manager.py
│  │  ├─ models.py
│  │  ├─ schemas.py
│  │  ├─ utils.py
│  ├─ htmlcov/
│  │  ├─ class_index.html
│  ├─ operations/
│  │  ├─ models.py
│  │  ├─ router.py
│  │  ├─ schemas.py
│  ├─ config.py
│  ├─ database.py
│  ├─ main.py
├─ migrations/
├─ postman-tests/
├─ tests/
│  ├─ auth_test.py
│  ├─ conftest.py
│  ├─ operations_test.py
├─ .gitignore
├─ .env
├─ pyproject.toml
├─ requirements.txt
├─ alembic.ini
```

1. src/ - contains common models, configs, and constants, etc.
    1. auth/ - contains all the models, schemas, configs that are essential for registretion and authentification processes;
<img src=https://github.com/Anastasiia-Pov/FastAPI_pet-project_to-do_list/blob/main/backend/backend_visuals/Auth.png width=450 />

2. operations/ - contains all the models, schemas, endpoints for working with tasks (add, edit, delete task)
<img src=https://github.com/Anastasiia-Pov/FastAPI_pet-project_to-do_list/blob/main/backend/backend_visuals/Tasks.png width=450 />

###### e.g. Get request: get all tasks (filter is implemented to filter tasks according to the user, priority and status)
<img src=https://github.com/Anastasiia-Pov/FastAPI_pet-project_to-do_list/blob/main/backend/backend_visuals/get%3Atasks.png width=450 />

```
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
```

Frontend is implemented by [StRenedas] (https://github.com/StRenedas).
