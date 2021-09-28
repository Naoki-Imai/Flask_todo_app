"""empty message

Revision ID: 0de6d9830093
Revises: 9a130beab367
Create Date: 2021-09-28 17:59:07.805858

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0de6d9830093'
down_revision = '9a130beab367'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_categories_category_name', table_name='categories')
    op.create_index(op.f('ix_categories_category_name'), 'categories', ['category_name'], unique=True)
    op.drop_constraint('categories_ibfk_1', 'categories', type_='foreignkey')
    op.drop_column('categories', 'todo_id')
    op.alter_column('todos', 'limit_date',
               existing_type=mysql.DATETIME(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'limit_date',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.add_column('categories', sa.Column('todo_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('categories_ibfk_1', 'categories', 'todos', ['todo_id'], ['id'])
    op.drop_index(op.f('ix_categories_category_name'), table_name='categories')
    op.create_index('ix_categories_category_name', 'categories', ['category_name'], unique=False)
    # ### end Alembic commands ###
