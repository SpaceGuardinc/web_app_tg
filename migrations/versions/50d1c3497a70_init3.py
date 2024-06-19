"""init3

Revision ID: 50d1c3497a70
Revises: b3f5906f167e
Create Date: 2024-03-21 14:41:52.455898

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '50d1c3497a70'
down_revision: Union[str, None] = 'b3f5906f167e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'product_photo_blob',
               existing_type=postgresql.BYTEA(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'product_photo_blob',
               existing_type=postgresql.BYTEA(),
               nullable=True)
    # ### end Alembic commands ###
