"""Initial migration

Revision ID: 4a40dbfedcc8
Revises: 
Create Date: 2025-07-16 00:23:25.588037

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '4a40dbfedcc8'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
	op.create_table('users',
		sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
		sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
		sa.Column('encrypted_password', sa.VARCHAR(), autoincrement=False, nullable=False),
		sa.PrimaryKeyConstraint('id', name=op.f('users_pkey'))
	)
	op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
	op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)

def downgrade() -> None:
	op.drop_index(op.f('ix_users_email'), table_name='users')
	op.drop_index(op.f('ix_users_id'), table_name='users')
	op.drop_table('users')
