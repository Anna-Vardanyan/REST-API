"""Add description column to Operator

Revision ID: 5cf2e220d28b
Revises: add_meta_data_column_connection
Create Date: 2024-12-28 03:12:33.738113

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'add_description_column_operator'
down_revision: Union[str, None] = 'add_meta_data_column_connection'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('operator', sa.Column('description', sa.String(length=255), nullable=True))


def downgrade() -> None:
    op.drop_column('operator', 'description')