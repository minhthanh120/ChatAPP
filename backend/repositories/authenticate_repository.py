from database.models import UserAuth, Session
from database.schemas import Login, User, Register, Token
from fastapi import HTTPException, Depends
from repositories.user_repository import user_repo as user_repository

from main import get_session
from utils import get_hashed_password, verify_password, create_refresh_token, create_access_token
from fastapi import status


class AuthorizeRepository:
    def __init__(self):
        self.session: Session = get_session().__next__()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            # rollback and let the exception propagate
            self.session.rollback()
            return False
        self.session.commit()
        return True

    def register(self, register: Register):
        try:
            currentUser: UserAuth = self.session.query(UserAuth).filter(UserAuth.email == register.email).first()
            if (currentUser == None):
                user = UserAuth()
                user.email = register.email
                password = get_hashed_password(register.password)
                user.password = password
                self.session.add(user)
                self.session.commit()
                user_repository.create(user)
                return {
                    "access_token": create_access_token(user.id),
                    "refresh_token": create_refresh_token(user.id)
                }
            return HTTPException(status.HTTP_409_CONFLICT, 'Already have account using this email')
        except Exception:
            self.session.rollback()
            return HTTPException(404, "An exception occurred")

    def login(self, login: Login):
        currentUser: UserAuth = self.session.query(UserAuth).filter(UserAuth.email == login.username).first()
        if (currentUser != None):
            if (verify_password(login.password, currentUser.password)):
                return {
                    "access_token": create_access_token(currentUser.id),
                    "refresh_token": create_refresh_token(currentUser.id)
                }
            else:
                return HTTPException(status.HTTP_401_UNAUTHORIZED, 'Password not right')
        return HTTPException(status.HTTP_404_NOT_FOUND, 'Not found User')

    def currentUser(self, token: str):
        pass

    def edit(self, session):
        pass

    def read(self, session):
        pass

    def delete(self, session):
        pass

    def authenticate(self, Login: Login):
        session = Session()
        try:
            # isUser = session.query(UserAuth).filter_by(userName = Login.userName, hashedPassword.encriptedValue = Login.password).first() is not None
            a = 'ok'
        finally:
            session.close()
        return isUser

# change user password
authorize_repo = AuthorizeRepository()