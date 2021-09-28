"""empty message

Revision ID: 6e74d681737d
Revises: 0de6d9830093
Create Date: 2021-09-28 18:00:22.594798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e74d681737d'
down_revision = '0de6d9830093'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('category_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'todos', 'categories', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todos', type_='foreignkey')
    op.drop_column('todos', 'category_id')
    # ### end Alembic commands ###
