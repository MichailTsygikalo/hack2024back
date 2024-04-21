"""fix sales

Revision ID: a5b60af1a702
Revises: e060fe79e2dc
Create Date: 2024-04-21 03:58:05.865778

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a5b60af1a702'
down_revision: Union[str, None] = 'e060fe79e2dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sales', sa.Column('service_id', sa.Integer(), nullable=False))
    op.drop_constraint('sales_contractor_id_fkey', 'sales', type_='foreignkey')
    op.create_foreign_key(None, 'sales', 'service', ['service_id'], ['id'], ondelete='cascade')
    op.drop_column('sales', 'contractor_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sales', sa.Column('contractor_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'sales', type_='foreignkey')
    op.create_foreign_key('sales_contractor_id_fkey', 'sales', 'contractor', ['contractor_id'], ['id'], ondelete='CASCADE')
    op.drop_column('sales', 'service_id')
    # ### end Alembic commands ###
