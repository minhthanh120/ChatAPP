from fastapi import APIRouter, Depends, HTTPException, status, Response
from database.models import Session
from database.schemas import UserSchema
from security import reuasble_oauth2
from main import get_session
from repositories.user_repository import user_repo as user_repository
from security import get_current_user

user_router = APIRouter()


@user_router.get("/")
def _get_current_user(user: UserSchema = Depends(get_current_user)):
    return user


@user_router.post("/edit")
def _edit_user(user:UserSchema, session: Session = Depends(get_session)):
    try:
        if(user_repository.read(user.id) == None):
            return HTTPException(status.HTTP_404_NOT_FOUND, "Not found user")
        user_repository.edit(user)
        return {"Edited successfull"}
    except:
        return HTTPException(404, "An exception occurred")
@user_router.get("/searchbyEmail/{key}")
def _searchbyEmail(key:str):
    try:
        if(len(key)>0):
            lstUser = user_repository.searchbyEmail(key)
            return lstUser
    except:
        return HTTPException(404, "An exception occurred")

