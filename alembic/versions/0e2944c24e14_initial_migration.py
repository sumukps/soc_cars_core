"""initial migration

Revision ID: 0e2944c24e14
Revises: 
Create Date: 2023-11-04 18:09:12.426640

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0e2944c24e14'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('car',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('car_type', sa.String(), nullable=True),
    sa.Column('available_count', sa.Integer(), nullable=False),
    sa.Column('rent_per_day', sa.Float(), nullable=False),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_car_id'), 'car', ['id'], unique=False)
    op.create_table('user_rental',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('car_id', sa.Integer(), nullable=True),
    sa.Column('rented_car_count', sa.Integer(), nullable=False),
    sa.Column('user_requested_duration_in_days', sa.Integer(), nullable=False),
    sa.Column('rental_started', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('rental_end_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('total_rent', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['car_id'], ['car.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_rental')
    op.drop_index(op.f('ix_car_id'), table_name='car')
    op.drop_table('car')
    op.drop_table('user')
    # ### end Alembic commands ###
