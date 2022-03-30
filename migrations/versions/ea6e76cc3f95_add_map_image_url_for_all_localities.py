"""Add map image url for all localities

Revision ID: ea6e76cc3f95
Revises: a3998bc31595
Create Date: 2022-01-18 15:27:11.236000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea6e76cc3f95'
down_revision = 'a3998bc31595'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('area_one', sa.Column('map_image_url', sa.String(), nullable=True))
    op.add_column('area_two', sa.Column('map_image_url', sa.String(), nullable=True))
    op.add_column('country', sa.Column('map_image_url', sa.String(), nullable=True))
    op.add_column('locality', sa.Column('map_image_url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('locality', 'map_image_url')
    op.drop_column('country', 'map_image_url')
    op.drop_column('area_two', 'map_image_url')
    op.drop_column('area_one', 'map_image_url')
    # ### end Alembic commands ###