"""Add columns to post table

Revision ID: 57723bff1c22
Revises: 16da43878aac
Create Date: 2024-06-05 20:31:11.174230

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '57723bff1c22'
down_revision: Union[str, None] = '16da43878aac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'posts', sa.Column('published', sa.Boolean(),
                           nullable=False, server_default='TRUE')
    )
    op.add_column(
        'posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                           nullable=False, server_default=sa.text(
                               'NOW()')
                           ))


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
