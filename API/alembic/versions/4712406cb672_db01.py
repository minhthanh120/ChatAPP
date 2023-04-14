"""db01

Revision ID: 4712406cb672
Revises: 
Create Date: 2023-04-13 22:46:57.574288

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision = '4712406cb672'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Group',
    sa.Column('Id', sa.NVARCHAR(length=450), nullable=False),
    sa.Column('GroupName', sa.String(), nullable=True),
    sa.Column('CreatedTime', sa.DateTime(), nullable=True),
    sa.Column('CreatorId', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('JoinRequest',
    sa.Column('Id', sa.NVARCHAR(length=450), nullable=False),
    sa.Column('CreatedTime', sa.DateTime(), nullable=True),
    sa.Column('CreatorId', sa.String(), nullable=True),
    sa.Column('GroupId', sa.String(), nullable=True),
    sa.Column('Accepted', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('JoinedMember',
    sa.Column('Id', sa.NVARCHAR(length=450), nullable=False),
    sa.Column('GroupId', sa.String(), nullable=True),
    sa.Column('MemberId', sa.String(), nullable=True),
    sa.Column('JoinedTime', sa.DateTime(), nullable=True),
    sa.Column('Role', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('Message',
    sa.Column('Id', sa.NVARCHAR(length=450), nullable=False),
    sa.Column('Content', sa.String(length=255), nullable=True),
    sa.Column('CreatedTime', sa.DateTime(), nullable=True),
    sa.Column('GroupId', sa.String(), nullable=True),
    sa.Column('SenderId', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('UserInfo',
    sa.Column('Id', sa.NVARCHAR(length=450), nullable=False),
    sa.Column('UserName', sa.String(length=50), nullable=True),
    sa.Column('FirstName', sa.String(length=25), nullable=True),
    sa.Column('LastName', sa.String(length=25), nullable=True),
    sa.Column('Email', sa.String(length=100), nullable=True),
    sa.Column('Avatar', sa.String(length=255), nullable=True),
    sa.Column('Phone', sa.String(length=11), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
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
    sa.PrimaryKeyConstraint('diagram_id', name='PK__sysdiagr__C2B05B611504F2B1')
    )
    op.drop_table('UserInfo')
    op.drop_table('Message')
    op.drop_table('JoinedMember')
    op.drop_table('JoinRequest')
    op.drop_table('Group')
    # ### end Alembic commands ###
