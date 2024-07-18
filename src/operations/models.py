from sqlalchemy import (ForeignKey, Table, Column, Integer, String, TIMESTAMP,
                        MetaData)

metadata = MetaData()

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
