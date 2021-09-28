"""empty message

Revision ID: 09129130b160
Revises: 6e74d681737d
Create Date: 2021-09-28 18:10:41.945843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09129130b160'
down_revision = '6e74d681737d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'todos', 'categories', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todos', type_='foreignkey')
    # ### end Alembic commands ###