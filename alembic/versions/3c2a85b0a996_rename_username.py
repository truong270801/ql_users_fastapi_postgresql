"""rename_username

Revision ID: 3c2a85b0a996
Revises: 8bcdc8b0087d
Create Date: 2024-05-06 15:38:01.327280

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3c2a85b0a996'
down_revision: Union[str, None] = '8bcdc8b0087d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('users', 'user_name', new_column_name='username', type_=sa.String(length=255))


def downgrade() -> None:
    pass
