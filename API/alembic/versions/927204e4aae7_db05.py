"""db05

Revision ID: 927204e4aae7
Revises: d4b78d6ed8b8
Create Date: 2023-04-15 23:48:30.986765

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision = '927204e4aae7'
down_revision = 'd4b78d6ed8b8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sysdiagrams')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sysdiagrams',
    sa.Column('name', sa.NVARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('principal_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('diagram_id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('version', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('definition', mssql.VARBINARY(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('diagram_id', name='PK__sysdiagr__C2B05B61EFBFAD2B')
    )
    # ### end Alembic commands ###