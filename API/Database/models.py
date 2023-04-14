from sqlalchemy import create_engine,NVARCHAR, Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import validates, declarative_base, Mapped, relationship
from sqlalchemy.engine import URL
import pyodbc
#import connection
CONNECTION_STRING = "Driver={ODBC Driver 17 for SQL Server};Server=SERAPHINE\\SQLEXPRESS;Database=CHATAPP;Trusted_Connection=Yes;MultipleActiveResultSets=true"
#CONNECTION_STRING = "mssql+pyodbc://SERAPHINE\SQLEXPRESS/CHATAPP"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": CONNECTION_STRING})
engine = create_engine(connection_url)
Base = declarative_base()

class Login():
    userName :str
    password :str
class Register():
    userName :str
    password :str
    confirmPassword :str

class User(Base):
    __tablename__ = 'UserInfo'
    id = Column('Id', NVARCHAR(450), primary_key= True)
    userName = Column('UserName', String(50))
    firstName = Column('FirstName', String(25))
    lastName = Column('LastName', String(25))
    email = Column('Email', String(100))
    avatar = Column('Avatar', String(255))
    phone = Column('Phone', String(11), nullable=True)

class Group(Base):
    __tablename__ = 'Group'
    id = Column('Id', NVARCHAR(450), primary_key=True)
    groupName = Column('GroupName', String)
    createdTime = Column('CreatedTime', DateTime)
    creatorId = Column('CreatorId', String)

class JoinRequest(Base):
    __tablename__ = 'JoinRequest'
    id = Column('Id', NVARCHAR(450), primary_key=True)
    createdTime = Column('CreatedTime', DateTime)
    creatorId = Column('CreatorId', String)
    groupId = Column('GroupId', String)
    accepted = Column('Accepted', Boolean)

class JoinedMember(Base):
    __tablename__ = 'JoinedMember'
    id = Column('Id', NVARCHAR(450), primary_key=True)
    groupId = Column('GroupId', String)
    memberId = Column('MemberId', String)
    joinedTime = Column('JoinedTime', DateTime)
    role = Column('Role', Integer)

class Message(Base):
    __tablename__ = 'Message'
    id = Column('Id', NVARCHAR(450), primary_key=True)
    content = Column('Content', String(255))
    createdTime = Column('CreatedTime', DateTime)
    groupId = Column('GroupId', String)
    senderId = Column('SenderId', String)

# if __name__ == '__main__':
#     conn = pyodbc.connect(CONNECTION_STRING)