from Database.models import Session, User, UserAuth, UserPassword
from Repositories import authenticate_repository
from fastapi import HTTPException, Response
from fastapi.responses import JSONResponse
from sqlalchemy.orm import lazyload
def login(Login, session):
    user = session.query(UserAuth).filter(UserAuth.email == Login.email).options(lazyload(UserAuth.hashedPassword)).first()
    if user:
        if user.hashedPassword.encriptedValue == Login.password:
            currentUser = session.query(User).filter(User.email == Login.email).first()
            return currentUser
    return HTTPException(401, "Unauthorize")
    
def register(Register, session):
    user = session.query(UserAuth).filter(UserAuth.email == Register.email).first()
    if user:
        raise HTTPException(409, 'Already Exist this email')
    else:
        currentUser = UserAuth(email=Register.email)
        session.add(currentUser)
        session.commit()
        currentUser.hashedPassword = UserPassword(userId=currentUser.id,hashString = Register.password, saltString = Register.password, encriptedValue = Register.password)
        session.commit()
    return Response("Account created!")

def log_out():
    pass

def change_password(PasswordChange, session):
    user = authenticate_repository.read(PasswordChange.userId, session)
    if not user:
        return HTTPException(404, "User not found!")
    return authenticate_repository.edit(PasswordChange, session)