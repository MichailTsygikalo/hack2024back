"""passport date

Revision ID: d726bc8830a6
Revises: 41496a08e91d
Create Date: 2024-04-21 04:46:35.253396

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd726bc8830a6'
down_revision: Union[str, None] = '41496a08e91d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pasport', 'date_issue',
               existing_type=sa.DATE(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pasport', 'date_issue',
               existing_type=sa.DATE(),
               nullable=False)
    # ### end Alembic commands ###