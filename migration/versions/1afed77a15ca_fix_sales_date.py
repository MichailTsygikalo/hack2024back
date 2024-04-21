"""fix sales date

Revision ID: 1afed77a15ca
Revises: a5b60af1a702
Create Date: 2024-04-21 04:07:36.928839

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1afed77a15ca'
down_revision: Union[str, None] = 'a5b60af1a702'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sales', sa.Column('date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sales', 'date')
    # ### end Alembic commands ###
