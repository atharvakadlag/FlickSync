"""movie db added

Revision ID: 9348f2f750f9
Revises: ab13fc885221
Create Date: 2023-10-24 01:05:56.818980

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '9348f2f750f9'
down_revision: Union[str, None] = 'ab13fc885221'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie',
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('genre', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('release_year', sa.Integer(), nullable=False),
    sa.Column('director', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('cast', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('runtime', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('cover_image', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('trailer_url', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('interest')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('interest',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('genre', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('movie')
    # ### end Alembic commands ###
