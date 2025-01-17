"""empty message

Revision ID: a72a71563df0
Revises: 
Create Date: 2023-04-30 13:21:04.490225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a72a71563df0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('facts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('submitter', sa.String(length=20), nullable=True),
    sa.Column('fact', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('facts')
    # ### end Alembic commands ###
