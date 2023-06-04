from pydantic import BaseModel, constr, datetime_parse
from datetime import datetime
from typing import Optional
class User(BaseModel):
    id: constr(max_length=450)
    userName: constr(max_length=50) = None
    firstName: constr(max_length=25)
    lastName: constr(max_length=25)
    email: constr(max_length=100)
    avatar: constr(max_length=255) = None
    phone: Optional[constr(max_length=11)] = None
    joinedDate: datetime = None
class Group(BaseModel):
    id: constr(max_length=450) = None
    groupName: str
    createdTime: datetime = None
    creatorId: constr(max_length=450)
class JoinedMember(BaseModel):
    id: constr(max_length=450)
    groupId: constr(max_length=450)
    memberId: constr(max_length=450)
    joinedTime: datetime
    role: int

class JoinRequest(BaseModel):
    id: constr(max_length=450)
    createdTime: datetime
    creatorId: constr(max_length=450)
    groupId: constr(max_length=450)
    accepted: bool

class Message(BaseModel):
    id: constr(max_length=450)
    content: constr(max_length=255)
    createdTime: datetime
    groupId: constr(max_length=450)
    senderId: constr(max_length=450)


# authorize
class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    exp:str
    sub:str
    #username: str | None = None
class Register(BaseModel):
    email: str
    password: str
    confirmPassword: str

class PasswordChange(BaseModel):
    userId: str
    oldPassword: str
    newPassword: str
    confirmPassword: str

class UserAuth(BaseModel):
    id: constr(max_length=450)
    email: str = None
    userName: str
    isAuthenticated: bool = None

class UserPassword(BaseModel):
    userId: constr(max_length=450)
    password: str
    saltString: str
# Schema
class UserSchema(User):
    joinedGroup: Optional[list[JoinedMember]] = None
    sended: Optional[list[Message]] = None
    createdGroup: Optional[list[Group]] = None
    requested: Optional[list[JoinRequest]] = None

class GroupSchema(Group):
    messages: Optional[list[Message]] = []
    joined: Optional[list[JoinedMember]] = []
    requested: Optional[list[JoinRequest]] = []
    creator: Optional[User] = None

class JoinedMemberSchema(JoinedMember):
    group: Optional[Group] = None
    member: Optional[User] = None

class JoinRequestSchema(JoinRequest):
    group: Optional[Group] = None
    creator: Optional[User] = None

class MessageSchema(Message):
    sender: Optional[User] = None
    group: Optional[Group] = None

class UserPasswordSchema(UserPassword):
    user: Optional[UserAuth] = None
class UserAuthSchema(UserAuth):
    hashedPassword: Optional[UserPassword] = None
