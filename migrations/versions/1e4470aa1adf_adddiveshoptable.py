"""AddDiveShopTable

Revision ID: 1e4470aa1adf
Revises: 65edcc4c267c
Create Date: 2022-04-28 22:43:55.398970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e4470aa1adf'
down_revision = '65edcc4c267c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dive_shop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('fareharbor_url', sa.String(), nullable=True),
    sa.Column('address1', sa.String(), nullable=True),
    sa.Column('address2', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('zip', sa.String(), nullable=True),
    sa.Column('logo_img', sa.String(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('locality_id', sa.Integer(), nullable=True),
    sa.Column('area_two_id', sa.Integer(), nullable=True),
    sa.Column('area_one_id', sa.Integer(), nullable=True),
    sa.Column('country_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['area_one_id'], ['area_one.id'], ),
    sa.ForeignKeyConstraint(['area_two_id'], ['area_two.id'], ),
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ),
    sa.ForeignKeyConstraint(['locality_id'], ['locality.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dive_shop')
    # ### end Alembic commands ###
