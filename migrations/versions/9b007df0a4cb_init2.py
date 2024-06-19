"""init2

Revision ID: 9b007df0a4cb
Revises: 7235042cc482
Create Date: 2024-03-21 14:23:57.496902

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b007df0a4cb'
down_revision: Union[str, None] = '7235042cc482'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('product_photo_tg', sa.String(length=200), nullable=False))
    op.alter_column('product', 'product_photo',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.LargeBinary(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'product_photo',
               existing_type=sa.LargeBinary(),
               type_=sa.VARCHAR(length=200),
               existing_nullable=False)
    op.drop_column('product', 'product_photo_tg')
    # ### end Alembic commands ###