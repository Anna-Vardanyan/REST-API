"""Add metadata column with GIN index to Connection

Revision ID: 3fca4d6e44c4
Revises:
Create Date: 2024-12-28 03:14:53.048914

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSON


# revision identifiers, used by Alembic.
revision: str = 'add_meta_data_column_connection'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('connection', sa.Column('meta_data', JSON(), nullable=True))
    op.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm")
    op.execute("CREATE INDEX gin_meta_data_idx ON connection USING gin (CAST(meta_data AS text) gin_trgm_ops)")


def downgrade() -> None:
    op.execute("DROP INDEX gin_meta_data_idx")
    op.drop_column('connection', 'meta_data')