"""user_id unique

Revision ID: 9d7996af73f8
Revises: abb19f9b3a35
Create Date: 2024-04-20 20:46:26.457483

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9d7996af73f8'
down_revision: Union[str, None] = 'abb19f9b3a35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'contractor', ['user_id'])
    op.create_unique_constraint(None, 'people', ['user_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'people', type_='unique')
    op.drop_constraint(None, 'contractor', type_='unique')
    # ### end Alembic commands ###
