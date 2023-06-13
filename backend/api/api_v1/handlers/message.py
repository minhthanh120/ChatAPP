from fastapi import APIRouter, Depends, HTTPException

from database.models import Message
from database.schemas import UserSchema, MessageSchema
from repositories.message_repository import message_repo
from security import get_current_user

message_route = APIRouter()

@message_route.post("/add")
def _send_message(message: MessageSchema, user: UserSchema = Depends(get_current_user)):
    try:
        message_repo.create(message)
        return "Sent"
    except Exception as e:
        return HTTPException(404, "An exception occurred")


