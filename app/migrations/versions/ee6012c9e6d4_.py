"""empty message

Revision ID: ee6012c9e6d4
Revises: d1575054a0ab
Create Date: 2020-04-11 02:54:15.789108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee6012c9e6d4'
down_revision = 'd1575054a0ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('software')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('software',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
    sa.Column('service', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('version', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='software_pkey')
    )
    # ### end Alembic commands ###