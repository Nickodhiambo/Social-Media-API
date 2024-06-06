"""Add content table

Revision ID: 2031abc31240
Revises: b901580fe0b7
Create Date: 2024-06-05 19:41:55.706330

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2031abc31240'
down_revision: Union[str, None] = 'b901580fe0b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
