from Database.models import Group, JoinedMember
from Repositories import group_repository, request_repository, member_repository
from fastapi import HTTPException, Response
def create_group(group, session):
    pass

def read_group(group, session):
    pass
def accept_member():
    pass
def remove_member():
    pass
def read_members():
    pass
def edit_group(group, session):
    currentGroup = group_repository.read(group.id, session)
    if currentGroup:
        currentGroup = group
        session.commit()
        return Response("Group Edited", 200)
    else:
        HTTPException(404, "Group Not Found")
