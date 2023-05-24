from fastapi import APIRouter, Depends, HTTPException
from database.models import Session
from database.schemas import UserSchema
from security import reuasble_oauth2
from main import get_session
from repositories import user_repository

user_router = APIRouter()
@user_router.get("/User/{id}", dependencies=[Depends(reuasble_oauth2)])
def _get_current_user(id: str, session: Session = Depends(get_session)):
    return user_repository.read(id, session)
@user_router.post("/User/edit")
def _edit_user(user, session: Session = Depends(get_session)):
    return user_repository.edit(user, session)

@user_router.post("/user_edit")
def _user_edit(user: UserSchema, session: Session = Depends(get_session)):
    try:
        pass
    except:
        return HTTPException(404, "An exception occurred")