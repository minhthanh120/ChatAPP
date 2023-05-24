from fastapi import APIRouter, HTTPException, status, Depends
from database.schemas import Login, Register, Token
from database.models import Session
from main import get_session
from repositories import authenticate_repository

authorize_router = APIRouter()

@authorize_router.post("/login")
def login(data: Login, session: Session = Depends(get_session)):
    try:
        return authenticate_repository.login(data, session)
    except():
       return HTTPException(404, "An exception occurred")


@authorize_router.post("/register")
def register(data: Register, session: Session = Depends(get_session)):
    try:
        return authenticate_repository.register(data, session)
    except:
        return HTTPException(404, "An exception occurred")