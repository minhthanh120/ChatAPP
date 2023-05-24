from database.models import UserAuth, Session
from database.schemas import Login, User, Register, Token
from fastapi import HTTPException
from utils import get_hashed_password, verify_password, create_refresh_token, create_access_token
def createUser(user:User, session:Session):
    currentUser = session.get(User).filter(User.email == user.email)
    if (currentUser == None):
        session.add(user)
        session.commit()
        return 'Created Account'
    return HTTPException(409, 'Already have account using this email')
def register(register:Register, session:Session):
    currentUser = session.query(UserAuth).filter(UserAuth.email == register.email).first()
    if (currentUser == None):
        user = UserAuth()
        user.email = register.email
        password = get_hashed_password(register.password)
        user.password = password
        session.add(user)
        session.commit()
        return create_access_token(register.email)            
    return HTTPException(409, 'Already have account using this email')
def login(login, session:Session):
    currentUser = session.query(UserAuth).filter(UserAuth.email == login.username).first()
    if (currentUser != None):
        if(verify_password(login.password, currentUser.password)):
            return {
                "access_token": create_access_token(login.username),
                "refresh_token": create_refresh_token(login.username)
            }
        else:
            return HTTPException(401, 'Password not right')
    return HTTPException(404, 'Not found User')

def edit(session):
    pass
def read(session):
    pass
def delete(session):
    pass

def authenticate(Login:Login):
    session = Session()
    try:
        #isUser = session.query(UserAuth).filter_by(userName = Login.userName, hashedPassword.encriptedValue = Login.password).first() is not None
        a = 'ok'
    finally:
        session.close()
    return isUser

# change user password
