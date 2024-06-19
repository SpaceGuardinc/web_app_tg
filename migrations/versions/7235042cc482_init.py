"""init

Revision ID: 7235042cc482
Revises: 
Create Date: 2024-03-19 16:57:54.547261

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7235042cc482'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('admin_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('admin_telegram_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('admin_id')
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('telegram_id', sa.BIGINT(), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=True),
    sa.Column('second_name', sa.String(length=30), nullable=True),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.Column('phone_number', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('order',
    sa.Column('order_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('fast_order', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('order_id')
    )
    op.create_table('product',
    sa.Column('product_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('product_name', sa.String(length=100), nullable=False),
    sa.Column('product_description', sa.Text(), nullable=False),
    sa.Column('product_size', sa.String(length=30), nullable=False),
    sa.Column('product_brand', sa.String(length=30), nullable=False),
    sa.Column('product_sex', sa.String(length=30), nullable=False),
    sa.Column('product_category', sa.String(length=30), nullable=False),
    sa.Column('product_price', sa.Integer(), nullable=False),
    sa.Column('product_photo', sa.String(length=200), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['order.order_id'], ),
    sa.PrimaryKeyConstraint('product_id')
    )
    op.create_table('product_size',
    sa.Column('size_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('product_size', sa.String(length=30), nullable=False),
    sa.Column('product_price', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.product_id'], ),
    sa.PrimaryKeyConstraint('size_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_size')
    op.drop_table('product')
    op.drop_table('order')
    op.drop_table('user')
    op.drop_table('admin')
    # ### end Alembic commands ###