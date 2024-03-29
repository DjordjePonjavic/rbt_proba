"""empty message

Revision ID: c28d916c3b1c
Revises: 3e8e5917a71f
Create Date: 2019-07-09 15:36:56.462184

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c28d916c3b1c'
down_revision = '3e8e5917a71f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('measurement', sa.Column('timestamp', sa.DateTime(), nullable=False))
    op.alter_column('measurement', 'air_quality',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.alter_column('measurement', 'humidity',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.alter_column('measurement', 'temperature',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('measurement', 'temperature',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.alter_column('measurement', 'humidity',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.alter_column('measurement', 'air_quality',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.drop_column('measurement', 'timestamp')
    # ### end Alembic commands ###
