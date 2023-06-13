from fastapi.routing import APIRouter

from database.schemas import User
from repositories.member_repository import member_repo
from fastapi import Depends
test_route = APIRouter()
@test_route.post("/test1")
def _test_token(current_user: User = Depends()):
    return current_user

@test_route.get(("/test2"))
def _test_token2():
    return member_repo.isMember('E4B262D9-B49D-43DF-819B-E31C0BE73477', '70015124-db82-11ed-8428-70a6ccc4b566')
