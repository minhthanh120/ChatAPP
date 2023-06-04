from fastapi import APIRouter
from api.api_v1.handlers import authorize, user, message, group

router = APIRouter()
router.include_router(user.user_router, prefix="/user")
router.include_router(authorize.auth_route)
router.include_router(message.message_route, prefix="/message")
router.include_router(group.group_router, prefix="/group")
