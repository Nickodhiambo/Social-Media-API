"""Link users and post tables

Revision ID: 16da43878aac
Revises: 02e659a4f543
Create Date: 2024-06-05 20:19:55.294180

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '16da43878aac'
down_revision: Union[str, None] = '02e659a4f543'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'owner_id', sa.Integer(), nullable=False
    ))
    op.create_foreign_key('posts_users-fk', source_table='posts',
                          referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'],
                          ondelete='CASCADE')


def downgrade() -> None:
    op.drop_constraint('posts_users-fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
