"""db01

Revision ID: 06db96c19a0f
Revises: 
Create Date: 2023-06-01 09:38:24.566065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06db96c19a0f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('UserAuth',
    sa.Column('Id', sa.NVARCHAR(length=450), nullable=False),
    sa.Column('Email', sa.String(), nullable=True),
    sa.Column('UserName', sa.String(), nullable=True),
    sa.Column('IsAuthenticated', sa.Boolean(), nullable=True),
    sa.Column('HashedPassword', sa.String(), nullable=True),
    sa.Column('SaltString', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('UserInfo',
    sa.Column('Id', sa.NVARCHAR(length=450), nullable=False),
    sa.Column('UserName', sa.String(length=50), nullable=True),
    sa.Column('FirstName', sa.NVARCHAR(length=25), nullable=True),
    sa.Column('LastName', sa.NVARCHAR(length=25), nullable=True),
    sa.Column('Email', sa.String(length=100), nullable=True),
    sa.Column('Avatar', sa.String(length=255), nullable=True),
    sa.Column('Phone', sa.String(length=15), nullable=True),
    sa.Column('JoinedDate', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('Group',
    sa.Column('Id', sa.NVARCHAR(length=450), nullable=False),
    sa.Column('GroupName', sa.NVARCHAR(), nullable=True),
    sa.Column('CreatedTime', sa.DateTime(), nullable=True),
    sa.Column('CreatorId', sa.NVARCHAR(length=450), nullable=True),
    sa.ForeignKeyConstraint(['CreatorId'], ['UserInfo.Id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('Token',
    sa.Column('Id', sa.NVARCHAR(length=450), nullable=True),
    sa.Column('UserId', sa.NVARCHAR(length=450), nullable=False),
    sa.Column('TokenValue', sa.String(), nullable=True),
    sa.Column('CreatedTime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['UserId'], ['UserAuth.Id'], ),
    sa.PrimaryKeyConstraint('UserId')
    )
    op.create_table('JoinRequest',
    sa.Column('Id', sa.NVARCHAR(length=450), nullable=False),
    sa.Column('CreatedTime', sa.DateTime(), nullable=True),
    sa.Column('CreatorId', sa.NVARCHAR(length=450), nullable=True),
    sa.Column('GroupId', sa.NVARCHAR(length=450), nullable=True),
    sa.Column('Accepted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['CreatorId'], ['UserInfo.Id'], ),
    sa.ForeignKeyConstraint(['GroupId'], ['Group.Id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('JoinedMember',
    sa.Column('Id', sa.NVARCHAR(length=450), nullable=False),
    sa.Column('GroupId', sa.NVARCHAR(length=450), nullable=True),
    sa.Column('MemberId', sa.NVARCHAR(length=450), nullable=True),
    sa.Column('JoinedTime', sa.DateTime(), nullable=True),
    sa.Column('Role', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['GroupId'], ['Group.Id'], ),
    sa.ForeignKeyConstraint(['MemberId'], ['UserInfo.Id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('LastestMessage',
    sa.Column('GroupId', sa.NVARCHAR(length=450), nullable=False),
    sa.Column('MemberId', sa.NVARCHAR(length=450), nullable=False),
    sa.Column('MessageId', sa.NVARCHAR(length=450), nullable=True),
    sa.Column('WatchedTime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['GroupId'], ['Group.Id'], ),
    sa.ForeignKeyConstraint(['MemberId'], ['UserInfo.Id'], ),
    sa.PrimaryKeyConstraint('GroupId', 'MemberId')
    )
    op.create_table('Message',
    sa.Column('Id', sa.NVARCHAR(length=450), nullable=False),
    sa.Column('Content', sa.NVARCHAR(length=255), nullable=True),
    sa.Column('CreatedTime', sa.DateTime(), nullable=True),
    sa.Column('GroupId', sa.NVARCHAR(length=450), nullable=True),
    sa.Column('SenderId', sa.NVARCHAR(length=450), nullable=True),
    sa.ForeignKeyConstraint(['GroupId'], ['Group.Id'], ),
    sa.ForeignKeyConstraint(['SenderId'], ['UserInfo.Id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Message')
    op.drop_table('LastestMessage')
    op.drop_table('JoinedMember')
    op.drop_table('JoinRequest')
    op.drop_table('Token')
    op.drop_table('Group')
    op.drop_table('UserInfo')
    op.drop_table('UserAuth')
    # ### end Alembic commands ###
