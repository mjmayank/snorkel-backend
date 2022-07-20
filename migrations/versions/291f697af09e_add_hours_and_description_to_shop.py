"""add hours and description to shop

Revision ID: 291f697af09e
Revises: e26e3086f57c
Create Date: 2022-07-20 14:00:40.947274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '291f697af09e'
down_revision = 'e26e3086f57c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dive_shop', sa.Column('description', sa.String(), nullable=True))
    op.add_column('dive_shop', sa.Column('hours', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dive_shop', 'hours')
    op.drop_column('dive_shop', 'description')
    # ### end Alembic commands ###
