from sqlalchemy import create_engine, NVARCHAR, Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property
from sqlalchemy.sql import func
from typing import List
from sqlalchemy.orm import validates, declarative_base, Mapped, relationship, mapped_column, Session, sessionmaker, \
    column_property
from sqlalchemy.engine import URL
import pyodbc
from pydantic import BaseModel
from uuid import uuid4
from sqlalchemy.sql.coercions import name
from sqlalchemy.sql.elements import ExpressionClauseList
from helper import read_config
config = read_config()
# import connection
CONNECTION_STRING = config['ConnectionString']['EngineUrl']

connection_url = URL.create(
    "mssql+pyodbc", query={"odbc_connect": CONNECTION_STRING})
engine = create_engine(connection_url, echo=True)
Session = sessionmaker(bind=engine)


Base = declarative_base()


class User(Base):
    __tablename__ = 'UserInfo'
    id = mapped_column('Id', NVARCHAR(450), primary_key=True, default=uuid4)
    userName = mapped_column('UserName', String(50))
    firstName = mapped_column('FirstName', NVARCHAR(25))
    lastName = mapped_column('LastName', NVARCHAR(25))
    email = mapped_column('Email', String(100))
    avatar = mapped_column('Avatar', String(255), nullable=True)
    phone = mapped_column('Phone', String(15), nullable=True)
    status = mapped_column('Status', Integer, nullable=True)
    joinedDate = mapped_column(
        'JoinedDate', DateTime, nullable=True, default=func.now())
    joinedGroup: Mapped[List["JoinedMember"]] = relationship(
        back_populates='member')
    sent: Mapped[List["Message"]] = relationship(
        back_populates='sender')
    createdGroup: Mapped[List["Group"]] = relationship(
        back_populates='creator')
    requested: Mapped[List["JoinRequest"]] = relationship(
        back_populates="creator")
    #reverse_fullname = column_property(" ".join('{0} {1}'.format(firstName, lastName).split(" ")[::-1]))

    @hybrid_property
    def get_fullname(self):
        return self.firstName+" "+self.lastName

class Group(Base):
    __tablename__ = 'Group'
    id = mapped_column('Id', NVARCHAR(450), primary_key=True, default=uuid4)
    groupName = mapped_column('GroupName', NVARCHAR)
    createdTime = mapped_column('CreatedTime', DateTime, default=func.now())
    creatorId = mapped_column(
        'CreatorId', NVARCHAR(450), ForeignKey("UserInfo.Id"))
    status = mapped_column('Status', Integer, nullable=True)    
    messages: Mapped[List["Message"]] = relationship(
        back_populates="group")
    joined: Mapped[List["JoinedMember"]] = relationship(
        back_populates="group")
    requested: Mapped[List["JoinRequest"]] = relationship(
        back_populates="group")
    creator: Mapped[User] = relationship(
        back_populates='createdGroup')
    @hybrid_method
    def is_member(self, userId : str):
        if self.joined!=None or len(self.joined)>0:
            for i in self.joined:
                if i.memberId == userId:
                    return True
        return False


class LastestMessage(Base):
    __tablename__ = 'LastestMessage'
    groupId = mapped_column('GroupId', NVARCHAR(
        450), ForeignKey("Group.Id"), primary_key=True)
    memberId = mapped_column('MemberId', NVARCHAR(
        450), ForeignKey("UserInfo.Id"), primary_key=True)
    messageId = mapped_column('MessageId', NVARCHAR(450), nullable=True)
    watchedTime = mapped_column('WatchedTime', DateTime, nullable=True)
    status = mapped_column('Status', Integer, nullable=True)

class JoinRequest(Base):
    __tablename__ = 'JoinRequest'
    id = mapped_column('Id', NVARCHAR(450), primary_key=True, default=uuid4)
    createdTime = mapped_column('CreatedTime', DateTime, default=func.now())
    creatorId = mapped_column(
        'CreatorId', NVARCHAR(450), ForeignKey("UserInfo.Id"))
    groupId = mapped_column('GroupId', NVARCHAR(450), ForeignKey("Group.Id"))
    accepted = mapped_column('Accepted', Boolean)
    group: Mapped[Group] = relationship(
        back_populates='requested')
    creator: Mapped[User] = relationship(
        back_populates='requested')
    status = mapped_column('Status', Integer, nullable=True)


class JoinedMember(Base):
    __tablename__ = 'JoinedMember'
    id = mapped_column('Id', NVARCHAR(450), primary_key=True, default=uuid4)
    groupId = mapped_column('GroupId', NVARCHAR(450), ForeignKey('Group.Id'))
    memberId = mapped_column('MemberId', NVARCHAR(450),
                             ForeignKey('UserInfo.Id'))
    joinedTime = mapped_column('JoinedTime', DateTime, default=func.now())
    role = mapped_column('Role', Integer, nullable=True)
    status = mapped_column('Status', Integer, nullable=True)
    group: Mapped[Group] = relationship(back_populates='joined')
    member: Mapped[User] = relationship(
        back_populates='joinedGroup')


class Message(Base):
    __tablename__ = 'Message'
    id = mapped_column('Id', NVARCHAR(450), primary_key=True, default=uuid4)
    content = mapped_column('Content', NVARCHAR(255))
    createdTime = mapped_column('CreatedTime', DateTime, default=func.now())
    groupId = mapped_column('GroupId', NVARCHAR(450), ForeignKey('Group.Id'))
    senderId = mapped_column('SenderId', NVARCHAR(450),
                             ForeignKey('UserInfo.Id'))
    status = mapped_column('Status', Integer, nullable=True)
    sender: Mapped[User] = relationship(back_populates="sent")
    group: Mapped[Group] = relationship(
        back_populates="messages")
# Authenticate Models


class UserAuth(Base):
    __tablename__ = 'UserAuth'
    id = mapped_column('Id', NVARCHAR(450), primary_key=True, default=uuid4)
    email = mapped_column('Email', String)
    userName = mapped_column('UserName', String, nullable=True)
    isAuthenticated = mapped_column('IsAuthenticated', Boolean, nullable=True)
    password = mapped_column('HashedPassword', String)
    saltString = mapped_column('SaltString', String)
    status = mapped_column('Status', Integer, nullable=True)
    # password:Mapped["UserPassword"] = relationship(back_populates="user", lazy="joined")
# class UserPassword(Base):
#     __tablename__ = 'UserPassword'
#     userId = mapped_column('UserId', NVARCHAR(450), ForeignKey('UserAuth.Id'), primary_key=True)
#     password = mapped_column('HashedPassword', String)
#     saltString = mapped_column('SaltString', String)
#     user:Mapped[UserAuth] = relationship(back_populates="password", lazy="joined")


class Token(Base):
    __tablename__ = "Token"
    id = mapped_column('Id', NVARCHAR(450), default=uuid4)
    userId = mapped_column('UserId', NVARCHAR(
        450), ForeignKey('UserAuth.Id'), primary_key=True)
    tokenValue = mapped_column('TokenValue', NVARCHAR(450))
    createdTime = mapped_column('CreatedTime', DateTime, default=func.now())
    status = mapped_column('Status', Integer, nullable=True)

# if __name__ == '__main__':
#     conn = pyodbc.connect(CONNECTION_STRING)
