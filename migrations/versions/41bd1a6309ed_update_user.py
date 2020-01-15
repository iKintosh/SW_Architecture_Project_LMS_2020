"""update user

Revision ID: 41bd1a6309ed
Revises: 5ecf30375af9
Create Date: 2020-01-12 23:30:09.110821

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '41bd1a6309ed'
down_revision = '5ecf30375af9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_registered', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_registered')
    # ### end Alembic commands ###