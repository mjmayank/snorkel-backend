"""empty message

Revision ID: 4dc8f65f694c
Revises: 
Create Date: 2021-07-14 13:11:46.072079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4dc8f65f694c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('review', sa.Column('date_dived', sa.DateTime(), nullable=True))
    op.alter_column('spot', 'rating',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('spot', 'rating',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    op.drop_column('review', 'date_dived')
    # ### end Alembic commands ###