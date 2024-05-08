"""update_user_table

Revision ID: 8bcdc8b0087d
Revises: 9eb1d35ae9d7
Create Date: 2024-05-06 11:18:56.988439

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column ,Integer, String, DATE
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8bcdc8b0087d'
down_revision: Union[str, None] = '9eb1d35ae9d7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.add_column('users', sa.Column('user_name', sa.String(length=50), nullable=False, server_default=''))
     op.add_column('users', sa.Column('password', sa.String(length=100), nullable=False,  server_default=''))


def downgrade() -> None:
    pass
