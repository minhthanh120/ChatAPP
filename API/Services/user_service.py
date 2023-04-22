from fastapi import HTTPException
from Repositories import user_repository
# get uset infomation
def get_user(id, session):
    user = user_repository.read(currentUser.id, session)
    if not user:
        return HTTPException(404, "User not found!")
    else:
        return user
# edit user infomation
def edit_user(currentUser, session):
    user = user_repository.read(currentUser.id, session)
    if not user:
        return HTTPException(404, "User not found!")
    return user_repository.edit(currentUser, session)


    
