from sqlalchemy import create_engine,NVARCHAR, Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func
from typing import List
from sqlalchemy.orm import validates, declarative_base, Mapped, relationship, mapped_column, Session, sessionmaker
from sqlalchemy.engine import URL
import pyodbc
from pydantic import BaseModel
from uuid import uuid4
#import connection
CONNECTION_STRING = "Driver={ODBC Driver 17 for SQL Server};Server=SERAPHINE\\SQLEXPRESS;Database=CHATAPP;Trusted_Connection=Yes;MultipleActiveResultSets=true"

connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": CONNECTION_STRING})
engine = create_engine(connection_url)
Session = sessionmaker(bind = engine)


Base = declarative_base()
class User(Base):
    __tablename__ = 'UserInfo'
    id = mapped_column('Id', NVARCHAR(450), primary_key= True, default=uuid4)
    userName = mapped_column('UserName', String(50))
    firstName = mapped_column('FirstName', String(25))
    lastName = mapped_column('LastName', String(25))
    email = mapped_column('Email', String(100))
    avatar = mapped_column('Avatar', String(255))
    phone = mapped_column('Phone', String(11), nullable=True)
    joinedGroup: Mapped[List["JoinedMember"]] = relationship(back_populates='member', lazy="joined")
    sended:Mapped[List["Message"]] = relationship(back_populates='sender', lazy="joined")
    createdGroup:Mapped[List["Group"]] = relationship(back_populates='creator', lazy="joined")
    requested:Mapped[List["JoinRequest"]] = relationship(back_populates="creator", lazy="joined")

class Group(Base):
    __tablename__ = 'Group'
    id = mapped_column('Id', NVARCHAR(450), primary_key=True, default=uuid4)
    groupName = mapped_column('GroupName', String)
    createdTime = mapped_column('CreatedTime', DateTime, default=func.now())
    creatorId = mapped_column('CreatorId', NVARCHAR(450), ForeignKey("UserInfo.Id"))
    messages:Mapped[List["Message"]] = relationship(back_populates="group", lazy="joined")
    joined:Mapped[List["JoinedMember"]] = relationship(back_populates="group", lazy="joined")
    requested:Mapped[List["JoinRequest"]] = relationship(back_populates="group", lazy="joined")
    creator:Mapped[User] = relationship(back_populates='createdGroup', lazy="joined")

class JoinRequest(Base):
    __tablename__ = 'JoinRequest'
    id = mapped_column('Id', NVARCHAR(450), primary_key=True, default=uuid4)
    createdTime = mapped_column('CreatedTime', DateTime, default=func.now())
    creatorId = mapped_column('CreatorId', NVARCHAR(450), ForeignKey("UserInfo.Id"))
    groupId = mapped_column('GroupId', NVARCHAR(450), ForeignKey("Group.Id"))
    accepted = mapped_column('Accepted', Boolean)
    group:Mapped[Group] = relationship(back_populates='requested', lazy="joined")
    creator:Mapped[User] = relationship(back_populates='requested', lazy="joined")

class JoinedMember(Base):
    __tablename__ = 'JoinedMember'
    id = mapped_column('Id', NVARCHAR(450), primary_key=True, default=uuid4)
    groupId = mapped_column('GroupId', NVARCHAR(450), ForeignKey('Group.Id'))
    memberId = mapped_column('MemberId', NVARCHAR(450), ForeignKey('UserInfo.Id'))
    joinedTime = mapped_column('JoinedTime', DateTime, default=func.now())
    role = mapped_column('Role', Integer)
    group:Mapped[Group] = relationship(back_populates='joined', lazy="joined")
    member:Mapped[User] = relationship(back_populates='joinedGroup', lazy="joined")

class Message(Base):
    __tablename__ = 'Message'
    id = mapped_column('Id', NVARCHAR(450), primary_key=True, default=uuid4)
    content = mapped_column('Content', String(255))
    createdTime = mapped_column('CreatedTime', DateTime, default=func.now())
    groupId = mapped_column('GroupId', NVARCHAR(450),ForeignKey('Group.Id'))
    senderId = mapped_column('SenderId', NVARCHAR(450), ForeignKey('UserInfo.Id'))
    sender:Mapped[User] = relationship(back_populates="sended", lazy="joined")
    group:Mapped[Group] = relationship(back_populates="messages", lazy="joined")
#Authenticate Models
class UserAuth(Base):
    __tablename__ = 'UserAuth'
    id = mapped_column('Id', NVARCHAR(450), primary_key=True, default=uuid4)
    email = mapped_column('Email', String, nullable=True)
    userName = mapped_column('UserName', String)
    isAuthenticated = mapped_column('IsAuthenticated', Boolean, nullable=True)
    hashedPassword:Mapped["UserPassword"] = relationship(back_populates="user", lazy="joined")
class UserPassword(Base):
    __tablename__ = 'UserPassword'
    userId = mapped_column('UserId', NVARCHAR(450), ForeignKey('UserAuth.Id'), primary_key=True)
    hashString = mapped_column('HashString', String)
    saltString = mapped_column('SaltString', String)
    encriptedValue = mapped_column('EncriptedValue', String)
    user:Mapped[UserAuth] = relationship(back_populates="hashedPassword", lazy="joined")
class Token(Base):
    __tablename__ = "Token"
    id = mapped_column('Id', NVARCHAR(450), default=uuid4)
    userId = mapped_column('UserId', NVARCHAR(450), ForeignKey('UserAuth.Id'), primary_key=True)
    tokenValue = mapped_column('TokenValue', String)
    createdTime = mapped_column('CreatedTime', DateTime, default=func.now())


# if __name__ == '__main__':
#     conn = pyodbc.connect(CONNECTION_STRING)