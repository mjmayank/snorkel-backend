"""Add difficulty field for spots

Revision ID: e523bfa64a19
Revises: 32a2a71c845c
Create Date: 2021-08-13 09:09:33.578354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e523bfa64a19'
down_revision = '32a2a71c845c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('spot', sa.Column('difficulty', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('spot', 'difficulty')
    # ### end Alembic commands ###
