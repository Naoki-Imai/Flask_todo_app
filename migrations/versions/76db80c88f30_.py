"""empty message

Revision ID: 76db80c88f30
Revises: 01a7ce8630be
Create Date: 2021-09-26 20:54:41.200862

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76db80c88f30'
down_revision = '01a7ce8630be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('limit_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'limit_date')
    # ### end Alembic commands ###
