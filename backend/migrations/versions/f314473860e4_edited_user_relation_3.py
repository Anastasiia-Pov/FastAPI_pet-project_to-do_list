"""edited User relation 3

Revision ID: f314473860e4
Revises: b0e2aa1cc0b5
Create Date: 2024-07-17 19:22:32.079089

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f314473860e4'
down_revision: Union[str, None] = 'b0e2aa1cc0b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tasks', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.drop_column('tasks', 'user_id')
    # ### end Alembic commands ###
