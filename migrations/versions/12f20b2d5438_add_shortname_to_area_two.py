"""Add shortname to area two

Revision ID: 12f20b2d5438
Revises: 5b88d4325fc4
Create Date: 2021-08-11 22:45:07.291180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12f20b2d5438'
down_revision = '5b88d4325fc4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('area_two', sa.Column('short_name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('area_two', 'short_name')
    # ### end Alembic commands ###
