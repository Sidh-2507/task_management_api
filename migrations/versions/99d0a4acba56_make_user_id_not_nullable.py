"""Make user_id not nullable

Revision ID: 99d0a4acba56
Revises: 9483c61ff7c5
Create Date: 2025-01-14 20:44:52.983140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99d0a4acba56'
down_revision = '9483c61ff7c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
