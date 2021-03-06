"""fix_col_2

Revision ID: dd38ae893dbb
Revises: 013e9d54f287
Create Date: 2022-06-16 17:23:03.313607

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'dd38ae893dbb'
down_revision = '013e9d54f287'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('mktcapmult', 'price_sales_ratio')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pedata', sa.Column('aggregate_markcap_to_trailing_net_income_ratio_only_money_makin', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
