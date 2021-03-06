"""Add hometown field on user

Revision ID: fa8290e9dddd
Revises: 91db0f46f796
Create Date: 2021-09-10 13:46:44.991300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa8290e9dddd'
down_revision = '91db0f46f796'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('hometown', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'hometown')
    # ### end Alembic commands ###
