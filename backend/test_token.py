from fastapi.routing import APIRouter

from database.schemas import User
from repositories.member_repository import member_repo
from  repositories.group_repository import group_repo
from fastapi import Depends
test_route = APIRouter()
@test_route.post("/test1")
def _test_token(current_user: User = Depends()):

    return current_user

@test_route.get(("/test2"))
def _test_token2():
    return group_repo.read('78A212DB-926A-4828-85A3-E62E94A2CDF8', True, True)
