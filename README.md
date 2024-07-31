# FastAPI_pet-project_to-do_list

## Project is motivated by learning backend using FastAPI and FastAPI Users frameworks, PostgreSQL, SQLAlchemy and PyTest.
## Project structure: Backend

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
├─ env_example.py
├─ pyproject.toml
├─ requirements.txt
├─ alembic.ini
```

1. [src/] (https://github.com/Anastasiia-Pov/FastAPI_pet-project_to-do_list/tree/main/backend/src) - contains common models, configs, and constants, etc.:
    - Authentification and registration of users implemented using FastApiUsers framework;
    - Database - PostgreSQL, work with DB is carried out by SQLAlchemy ORM;
    - Authentification transport is cookie;
    - Authentification strategy is JWTStrategy;

    1. auth/ - contains all the models, schemas, configs that are essential for registretion and authentification processes;
<img src=https://github.com/Anastasiia-Pov/FastAPI_pet-project_to-do_list/blob/main/backend/backend_visuals/Auth.png width=450 />

2. operations/ - contains all the models, schemas, endpoints for working with tasks (add, edit, delete task)
<img src=https://github.com/Anastasiia-Pov/FastAPI_pet-project_to-do_list/blob/main/backend/backend_visuals/Tasks.png width=450 />

#### e.g. Get request: get all tasks (filter is implemented to filter tasks according to the user, priority and status)
Other endpoints are available in src/operations/router.py
<img src=https://github.com/Anastasiia-Pov/FastAPI_pet-project_to-do_list/blob/main/backend/backend_visuals/get%3Atasks.png width=450 />

3. tests/ - contains files to execute tests with pytest. Coverage is performed by coverage.py. Percantage of coverage is 84%.
<img src=https://github.com/Anastasiia-Pov/FastAPI_pet-project_to-do_list/blob/main/backend/backend_visuals/coverage_pytests.png width=750 />

4. env_example.py - is for .env, contains all the necessary variable that are needed to be specified.

## Frontend is implemented by [StRenedas] (https://github.com/StRenedas).
