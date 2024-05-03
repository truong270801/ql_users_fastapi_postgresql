"""create users table

Revision ID: 9eb1d35ae9d7
Revises: 
Create Date: 2024-05-03 09:52:23.874046

"""
from typing import Sequence, Union

from alembic import op
from models.model import User

# revision identifiers, used by Alembic.
revision: str = '9eb1d35ae9d7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
       User.__table__.create(bind=op.get_bind())

def downgrade() -> None:
    pass
