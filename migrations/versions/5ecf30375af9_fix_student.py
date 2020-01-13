"""fix Student

Revision ID: 5ecf30375af9
Revises: 12b0e8390634
Create Date: 2020-01-12 12:44:34.238439

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '5ecf30375af9'
down_revision = '12b0e8390634'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('is_pay', sa.Boolean(), nullable=True))
    op.drop_column('student', 'pay_flg')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('pay_flg', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('student', 'is_pay')
    # ### end Alembic commands ###