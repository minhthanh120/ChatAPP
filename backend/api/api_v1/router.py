from fastapi import APIRouter
from api.api_v1.handlers import authorize, user

router = APIRouter()
router.include_router(user.user_router)
router.include_router(authorize.authorize_router)
