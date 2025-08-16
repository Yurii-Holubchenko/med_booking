"""add reset_password_token

Revision ID: 33b0fd665e65
Revises: 2691705b5f5a
Create Date: 2025-08-15 00:57:02.882625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '33b0fd665e65'
down_revision: Union[str, Sequence[str], None] = '2691705b5f5a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("reset_password_token", sa.String(), nullable=True))
    op.add_column("users", sa.Column("reset_password_token_expired_at", sa.DateTime(timezone=True), nullable=True))

def downgrade() -> None:
    op.drop_column("users", "reset_password_token")
    op.drop_column("users", "reset_password_token_expired_at")
