from fastapi.routing import APIRouter

from database.schemas import User

from fastapi import Depends
test_route = APIRouter()
@test_route.post("/test1")
def _test_token(current_user: User = Depends()):
    return current_user