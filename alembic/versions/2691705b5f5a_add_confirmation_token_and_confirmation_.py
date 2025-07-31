"""add confirmation_token and confirmation_token_expired_at to users

Revision ID: 2691705b5f5a
Revises: 213265f0130e
Create Date: 2025-07-25 22:38:02.691194

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '2691705b5f5a'
down_revision: Union[str, Sequence[str], None] = '213265f0130e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("confirmation_token", sa.String(), nullable=True))
    op.add_column("users", sa.Column('confirmation_token_expired_at', sa.DateTime(), nullable=True))

def downgrade() -> None:
    op.drop_column("users", "confirmation_token")
    op.drop_column("users", "confirmation_token_expired_at")
