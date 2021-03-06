"""empty message

Revision ID: a17bf09bdb60
Revises: 
Create Date: 2020-10-27 21:02:31.484174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a17bf09bdb60'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_income',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('city', sa.Integer(), nullable=True),
    sa.Column('job', sa.Integer(), nullable=True),
    sa.Column('basic', sa.Integer(), nullable=False),
    sa.Column('da', sa.Integer(), nullable=True),
    sa.Column('hra', sa.Integer(), nullable=True),
    sa.Column('conveyance', sa.Integer(), nullable=True),
    sa.Column('lta', sa.Integer(), nullable=True),
    sa.Column('others', sa.Integer(), nullable=True),
    sa.Column('rent', sa.Integer(), nullable=True),
    sa.Column('professional_tax', sa.Integer(), nullable=True),
    sa.Column('ac', sa.Integer(), nullable=True),
    sa.Column('ad', sa.Integer(), nullable=True),
    sa.Column('add', sa.Integer(), nullable=True),
    sa.Column('addb', sa.Integer(), nullable=True),
    sa.Column('ae', sa.Integer(), nullable=True),
    sa.Column('ag', sa.Integer(), nullable=True),
    sa.Column('agg', sa.Integer(), nullable=True),
    sa.Column('agga', sa.Integer(), nullable=True),
    sa.Column('aggc', sa.Integer(), nullable=True),
    sa.Column('atta', sa.Integer(), nullable=True),
    sa.Column('au', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_income')
    # ### end Alembic commands ###
