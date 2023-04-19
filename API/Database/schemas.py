from pydantic import BaseModel, constr
from datetime import datetime
from typing import List
class Login(BaseModel):
    userName:str
    password:str
class Register(BaseModel):
    userName :str
    password :str
    confirmPassword :str

class User(BaseModel):
    id : constr(max_length = 450)
    userName : constr(max_length=50)
    firstName : constr(max_length=25)
    lastName : constr(max_length=25)
    email : constr(max_length=100)
    avatar : constr(max_length=255)
    phone : constr(max_length=11) = None
    joinedGroup: List["JoinedMember"]
    sended:List["Message"]
    createdGroup:List["Group"] 
    requested:List["JoinRequest"]

class Group(BaseModel):
    id : constr(max_length = 450)
    groupName : str
    createdTime : datetime
    creatorId : constr(max_length=450)
    messages:List["Message"]
    joined:List["JoinedMember"]
    requested:List["JoinRequest"]
    creator:"User"

class JoinRequest(BaseModel):
    id : constr(max_length = 450)
    createdTime : datetime
    creatorId : constr(max_length=450)
    groupId : constr(max_length=450)
    accepted : bool
    group:"Group"
    creator:"User"

class JoinedMember(BaseModel):
    id : constr(max_length = 450)
    groupId : constr(max_length=450)
    memberId : constr(max_length=450)
    joinedTime = datetime
    role : int
    group:"Group"
    member:"User"
    

class Message(BaseModel):
    id : constr(max_length = 450)
    content : constr(max_length=255)
    createdTime : datetime
    groupId : constr(max_length=450)
    senderId : constr(max_length=450)
    sender:"User"
    group:"Group"
#Authenticate Models
class UserAuth(BaseModel):
    id : constr(max_length = 450)
    email : str = None
    userName : str
    isAuthenticated : bool = None
    hashedPassword:"UserPassword"
class UserPassword(BaseModel):
    userId : constr(max_length=450)
    hashString : str
    saltString : str
    encriptedValue : str
    user:"UserAuth"
class Token(BaseModel):
    id : constr(max_length = 450)
    userId : constr(max_length=450)
    tokenValue : str
    createdTime : datetime