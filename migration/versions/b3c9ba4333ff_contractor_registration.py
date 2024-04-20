"""contractor-registration

Revision ID: b3c9ba4333ff
Revises: 1935315da710
Create Date: 2024-04-20 20:43:14.963187

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b3c9ba4333ff'
down_revision: Union[str, None] = '1935315da710'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contractor', sa.Column('registration_id', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'contractor', ['name'])
    op.create_foreign_key(None, 'contractor', 'registration', ['registration_id'], ['id'], ondelete='cascade')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'contractor', type_='foreignkey')
    op.drop_constraint(None, 'contractor', type_='unique')
    op.drop_column('contractor', 'registration_id')
    # ### end Alembic commands ###
