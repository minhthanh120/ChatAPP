from typing import List

from fastapi import APIRouter, HTTPException, Depends
from starlette import status

from database.models import Group
from repositories.group_repository import group_repo
from database.schemas import GroupSchema, UserSchema
from repositories.member_repository import member_repo
from security import get_current_user

group_router = APIRouter()

@group_router.post("/add")
def _add_group(group: GroupSchema, members: List[UserSchema]):
    try:
        result = group_repo.create(group)
        for user in members:
            member_repo.create(result.id, user.id)
        member_repo.create(result.id, result.creatorId)
        return result
    except Exception as e:
        print(e)
        return HTTPException(404, "An exception occurred")
@group_router.get("/recentmessage")
def _get_recent_message(user:UserSchema = Depends(get_current_user)):
    try:
        recent = group_repo.get_recent(user.id)
        return recent
    except Exception as e:
        print(e)
        return HTTPException(404, "An exception occurred")

@group_router.get("/{id}")
def _get_group(id:str, user: UserSchema = Depends(get_current_user)):
    try:
        if member_repo.isMember(id, user.id) == False:
            return HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Method not allowed")
        group:Group = group_repo.read(id, True, True)
        return group
    except Exception as e:
        print(e)
        return HTTPException(404, "An exception occurred")

@group_router.get("/delete/{id}")
def _del_group(id:str, user: UserSchema = Depends(get_current_user)):
    try:
        if member_repo.isAdmin(id, user.id) == False:
            return HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Method not allowed")
        group_repo.delete(id)
        return
    except Exception as e:
        print(e)
        return HTTPException(404, "An exception occurred")

@group_router.post("/addmembers")
def _add_members(id: str, members: List[UserSchema], user: UserSchema = Depends(get_current_user)):
    try:
        if member_repo.isAdmin(id, user.id) == False:
            return HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Method not allowed")
    except Exception as e:
        print(e)
        return HTTPException(404, "An exception occurred")

@group_router.post("/addmember")
def _add_member(id: str, member: UserSchema, user: UserSchema = Depends(get_current_user)):
    try:
        if member_repo.isAdmin(id, user.id) == False:
            return HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Method not allowed")
    except Exception as e:
        print(e)
        return HTTPException(404, "An exception occurred")


@group_router.get("/allNotInGroup/{key}")
def _searchbyEmail(groupId:str):
    try:
        if(len(key)>0):
            lstUser = user_repository(key)
            return lstUser
    except:
        return HTTPException(404, "An exception occurred")
