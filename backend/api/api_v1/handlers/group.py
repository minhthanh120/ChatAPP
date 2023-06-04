from typing import List

from fastapi import APIRouter, HTTPException
from repositories.group_repository import group_repo
from database.schemas import GroupSchema, UserSchema
from repositories.member_repository import member_repo

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

@group_router.get("/{id}")
def _group(id:str):
    try:
        group = group_repo.read(id)
        return group
    except Exception as e:
        print(e)
        return HTTPException(404, "An exception occurred")