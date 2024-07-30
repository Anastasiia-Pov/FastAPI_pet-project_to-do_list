from sqlalchemy import (Table, Column, Integer, String)
from database import metadata, Base
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable


operation = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("task", String, nullable=False),
    Column("description", String, nullable=True),
    Column("priority", String, nullable=False),
    Column("status", String, nullable=False),
    Column("user_id", Integer, nullable=False, default=0)
)


class Tasks(Base):
    __tablename__ = 'tasks'
    # __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    task = Column("task", String, nullable=False)
    description = Column("description", String, nullable=True)
    priority = Column("priority", String, nullable=False)
    status = Column("status", String, nullable=False)
    user_id = Column("user_id", Integer, nullable=False, default=0)
