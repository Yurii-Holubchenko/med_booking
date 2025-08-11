"""add refresh_token, refresh_token_expired_at to users

Revision ID: 213265f0130e
Revises: 4a40dbfedcc8
Create Date: 2025-07-20 19:39:51.343168

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '213265f0130e'
down_revision: Union[str, Sequence[str], None] = '4a40dbfedcc8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("refresh_token", sa.String(), nullable=True))
    op.add_column("users", sa.Column("refresh_token_expired_at", sa.DateTime(timezone=True), nullable=True))

def downgrade() -> None:
    op.drop_column("users", "refresh_token")
    op.drop_column("users", "refresh_token_expired_at")
