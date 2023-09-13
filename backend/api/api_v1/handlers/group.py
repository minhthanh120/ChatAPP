from typing import List

from fastapi import APIRouter, HTTPException, Depends
from starlette import status

from repositories.group_repository import group_repo
from database.schemas import GroupSchema, UserSchema, Group
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
        if group_repo.read(id=id) == None:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This group has been deleted or never be created before")
        if member_repo.isMember(id, user.id) == False:
            return HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Method not allowed")
        group:Group = group_repo.read(id, True, True)
        return group
    except Exception as e:
        print(e)
        return HTTPException(404, "An exception occurred")
@group_router.post("/editinfo")
def _edit_groupinfo(group:GroupSchema, user:UserSchema = Depends(get_current_user)):
    try:
        if group_repo.read(id=group.id) == None:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This group has been deleted or never be created before")
        if member_repo.isMember(groupId = group.id,userId= user.id) == False:
            return HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Method not allowed")
        return group_repo.edit(group=group)
    except Exception as e:
        print(e)
        return HTTPException(404, "An exception occurred")        
@group_router.post("/editmembers")
def _edit_groupmembers(group:GroupSchema, user:UserSchema = Depends(get_current_user)):
    try:
        if group_repo.read(id=group.id) == None:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This group has been deleted or never be created before")
        if member_repo.isMember(groupId = group.id,userId= user.id) == False:
            return HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Method not allowed")
        return group_repo.edit(group=group)
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

@group_router.post("/addmember")
def _add_member(id: str, memberid:str, user: UserSchema = Depends(get_current_user)):
    try:
        if member_repo.isAdmin(id, user.id) == False:
            return HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Method not allowed")
        if member_repo.isMember(groupId=id, userId=memberid) == True or member_repo.isAdmin(groupId=id, userId=memberid) == True:
            return HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This member already in your group")
        return member_repo.create(groupId=id, memberId=memberid)
    except Exception as e:
        print(e)
        return HTTPException(404, "An exception occurred")

@group_router.post("/removemember")
def _remove_member(id: str, memberid: str, user: UserSchema = Depends(get_current_user)):
    try:
        if member_repo.isAdmin(id, user.id) == False:
            return HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Method not allowed")
        if member_repo.isMember(groupId=id, userId=memberid) == False:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Don't have this member in your group or this member has been kick-out")
        return member_repo.delete(groupId=id, memberId=memberid)
    except Exception as e:
        print(e)
        return HTTPException(404, "An exception occurred")


