from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import validates
class User(Model):
    _tablename_ = 'UserInfo'
    id = Column('Id', String, primary_key= True)
    userName = Column('UserName', String(50))
    firstName = Column('FirstName', String(25))
    lastName = Column('LastName', String(25))
    email = Column('Email', String(100))
    avatar = Column('Avatar', String(255))
    phone = Column('Phone', String(11))

class Group(Model):
    _tablename_ = 'Group'
    id = Column('Id', String, primary_key=True)
    groupName = Column('GroupName', String)
    createdTime = Column('CreatedTime', DateTime)
    creatorId = Column('CreatorId', String)

class JoinRequest(Model):
    _tablename_ = 'JoinRequest'
    id = Column('Id', String, primary_key=True)
    createdTime = Column('CreatedTime', DateTime)
    creatorId = Column('CreatorId', String)
    groupId = Column('GroupId', String)
    accepted = Column('Accepted', Boolean)

class JoinedMember(Model):
    _tablename_ = 'JoinedMember'
    id = Column('Id', String, primary_key=True)
    groupId = Column('GroupId', String)
    memberId = Column('MemberId', String)
    joinedTime = Column('JoinedTime', DateTime)
    role = Column('Role', Integer)

class Message(Model):
    _tablename_ = 'Message'
    id = Column('Id', String, primary_key=True)
    content = Column('Content', String(255))
    createdTime = Column('CreatedTime', DateTime)
    groupId = Column('GroupId', String)
    senderId = Column('SenderId', String)