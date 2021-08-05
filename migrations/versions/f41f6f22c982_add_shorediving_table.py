"""Add shorediving table

Revision ID: f41f6f22c982
Revises: 3b0f8dc881cf
Create Date: 2021-07-30 13:23:13.042599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f41f6f22c982'
down_revision = '3b0f8dc881cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shore_diving_review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shorediving_id', sa.String(), nullable=True),
    sa.Column('shorediving_url', sa.String(), nullable=True),
    sa.Column('review_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['review_id'], ['review.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shore_diving_review')
    # ### end Alembic commands ###