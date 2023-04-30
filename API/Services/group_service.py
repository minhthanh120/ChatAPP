from Database.models import Group, JoinedMember
from Repositories import group_repository, request_repository, member_repository
from fastapi import HTTPException, Response
def create_group(group, session):
    group = group_repository.read(id, session)
    if group == None:
        group_repository.create(group, session)
        return Response("Group Created", 201)
    return HTTPException(409, "Already have this group")

def get_group(id, session):
    currentGroup = group_repository.read(id, session)
    if currentGroup:
        return Response(currentGroup, 200)
    return HTTPException(404, "Group Not Found") 
def accept_request(id, session):
    pass
def remove_member(member, session):
    pass
def list_members(groupId, session):
    pass
def edit_group(group, session):
    currentGroup = group_repository.read(group.id, session)
    if currentGroup:
        group_repository.edit(currentGroup, session)
        return Response("Group Edited", 200)
    else:
        return HTTPException(404, "Group Not Found")
