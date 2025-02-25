"""Update Task model user_id nullable

Revision ID: 9483c61ff7c5
Revises: ad906be5e493
Create Date: 2025-01-14 19:23:01.610490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9483c61ff7c5'
down_revision = 'ad906be5e493'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
