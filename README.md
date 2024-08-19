# FastAPI_pet-project_to-do_list

## Project is motivated by learning backend using FastAPI and FastAPI Users web-frameworks, PostgreSQL, SQLAlchemy and PyTest.

### Requirements
Python 3.12 with all the [requirements.txt](https://github.com/Anastasiia-Pov/FastAPI_pet-project_to-do_list/blob/main/backend/requirements.txt) dependencies installed.

### Project structure: Backend

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
│  ├─ pages/
│  ├─ templates/
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
├─ .env.example
├─ pyproject.toml
├─ requirements.txt
├─ alembic.ini
```

Main points:
- Authentification and registration of users implemented using FastApiUsers framework;
- Database - PostgreSQL, work with DB is carried out with async by SQLAlchemy ORM;
- Authentification transport is cookie;
- Authentification strategy is JWTStrategy.

Files structure:
1. ```src/``` - contains common models, configs, and constants, etc.:

    - ```auth/``` - contains all the models, schemas, configs that are essential for registretion and authentification processes;
    - ```operations/``` - contains all the models, schemas, endpoints for working with tasks (add, edit, delete task);
    - ```main.py``` - entry point;

<img src=https://github.com/Anastasiia-Pov/FastAPI_pet-project_to-do_list/blob/main/backend/backend_visuals/Auth.png width=450 /> Fig. 1 Authentification endpoints
<img src=https://github.com/Anastasiia-Pov/FastAPI_pet-project_to-do_list/blob/main/backend/backend_visuals/Tasks.png width=450 /> Fig. 2 To-do List endpoints

#### e.g. Get request: get all tasks (filter is implemented to filter tasks according to the user, priority and status)
Other endpoints are available in [src/operations/router.py](https://github.com/Anastasiia-Pov/FastAPI_pet-project_to-do_list/blob/main/backend/src/operations/router.py)

<img src=https://github.com/Anastasiia-Pov/FastAPI_pet-project_to-do_list/blob/main/backend/backend_visuals/get%3Atasks.png width=450 />

3. ```tests/``` - contains files to execute tests with pytest. Coverage is performed by coverage.py. Percantage of coverage is 84%.
```class_index.html``` contains information presented below
<img src=https://github.com/Anastasiia-Pov/FastAPI_pet-project_to-do_list/blob/main/backend/backend_visuals/coverage_pytests.png width=800 />

4. ```postman-test``` - contains API tests with postman in JSON-file format.

5. ```.env.example``` - is for .env, contains all the necessary variable that are needed to be specified.

6. ```pages``` - contains routers for html layouts```templates``` - contains html layouts.

<img src=https://github.com/Anastasiia-Pov/FastAPI_pet-project_to-do_list/blob/main/backend/backend_visuals/html_layout_for_tasks_board.png>

### Implemented:
- password validation;
- email validation;

## Frontend is implemented by [StRenedas](https://github.com/StRenedas).
