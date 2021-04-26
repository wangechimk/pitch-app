"""update profile  migration

Revision ID: d64a89476e60
Revises: 0be36f0d6445
Create Date: 2021-04-26 23:51:45.313989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd64a89476e60'
down_revision = '0be36f0d6445'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    op.drop_column('users', 'profile_pic')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('profile_pic', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('users', 'profile_pic_path')
    # ### end Alembic commands ###
