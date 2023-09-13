from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from database.models import User, UserAuth
from database.schemas import Login, Register, ResetPassword
from repositories.authenticate_repository import authorize_repo as authenticate_repository
from  repositories.user_repository import user_repo as user_repository
from utils import create_access_token, create_refresh_token, get_hashed_password

auth_route = APIRouter()
@auth_route.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
    try:
        login = Login(username=form.username, password=form.password)
        return authenticate_repository.login(login)
    except():
       return HTTPException(404, "An exception occurred")


@auth_route.post("/register")
def register(register: Register):
    return authenticate_repository.register(register)

@auth_route.post("/refresh")
def _refresh_token():
    pass
@auth_route.post("/resetpassword")
def _reset_password(model: ResetPassword):
    return authenticate_repository.resetpassword(model=model)