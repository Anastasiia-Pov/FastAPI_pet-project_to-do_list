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
    i. auth/ - contains all the models, schemas, configs that are essential for registretion and authentification processes;
    ![Auth endpoints](https://github.com/Anastasiia-Pov/FastAPI_pet-project_to-do_list/blob/main/backend/backend_visuals/Auth.png)

####  Frontend is implemented by [StRenedas] (https://github.com/StRenedas).
