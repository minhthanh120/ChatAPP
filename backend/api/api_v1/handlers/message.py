from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from database.models import Message
from database.schemas import UserSchema, MessageSchema
from repositories.message_repository import message_repo
from repositories.group_repository import group_repo
from repositories.member_repository import member_repo
from security import get_current_user

message_route = APIRouter()

@message_route.post("/add")
def _send_message(message: MessageSchema, user: UserSchema = Depends(get_current_user)):
    try:
        if group_repo.read(id=message.groupId) == None:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This group has been deleted or never be created before")
        if member_repo.isMember(message.groupId, user.id) == False:
            return HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Method not allowed")
        m = Message()
        m.groupId = message.groupId
        m.senderId = message.senderId
        m.createdTime = message.createdTime
        m.content = message.content
        return message_repo.create(m)
    except Exception as e:
        return HTTPException(404, "An exception occurred")
@message_route.post("/edit")
def _edit_message(message: MessageSchema, user: UserSchema = Depends(get_current_user)):
    try:
        if message.senderId != user.id:
            return HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Method not allowed")
        if message_repo.read(message.id) == None:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This message has been deleted or never be created before")
        return message_repo.edit(message)
    except Exception as e:
        return HTTPException(404, "An exception occurred")

@message_route.post("/delete")
def _del_message(message: MessageSchema, user: UserSchema = Depends(get_current_user)):
    try:
        model = message_repo.read(message.id)
        if model == None:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This message has been deleted or never be created before")
        if model.senderId != user.id:
            return HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Method not allowed")
        return message_repo.delete(model.id)
    except Exception as e:
        return HTTPException(404, "An exception occurred")
@message_route.get("/recent")
def _get_recent_message(user: UserSchema = Depends(get_current_user)):
    try:
        rows = message_repo.recentMessage(user.id)
        return rows
    except Exception as e:
        return HTTPException(404, "An exception occurred")
