from Database.models import Session
from Database import models
import uuid
from sqlalchemy.orm import sessionmaker, lazyload
from typing import Union
from fastapi import FastAPI, HTTPException, Depends
from Services import user_service, authorize_service, group_service
import uvicorn
from datetime import datetime
from Database.schemas import Login, Register, GroupSchema, UserSchema
app = FastAPI()


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()


@app.get("/")
def read_foot():
    return {"Hello": "Hello"}


@app.get("/User/{id}")
def read_user(id: str):
    return {"id": id, "q": q}

@app.get("/Group/{id}")
def _read_group(id: str, session: Session = Depends(get_session)):
    return group_service.read_group(id, session)

@app.get("/Members/{id}")
def _read_Members(id: str, session: Session = Depends(get_session)):
    return group_service.read_members(id, session)


@app.post("/login")
def login(login: Login, session: Session = Depends(get_session)):
    try:
        return authorize_service.login(login, session)
    except:
        return HTTPException(404, "An exception occurred")


@app.post("/register")
def register(register: Register, session: Session = Depends(get_session)):
    try:
        return authorize_service.register(register, session)
    except:
        return HTTPException(404, "An exception occurred")


@app.post("/user_edit")
def _user_edit(user: UserSchema, session: Session = Depends(get_session)):
    try:
        return user_service.edit_user()
    except:
        return HTTPException(404, "An exception occurred")


@app.post("/group_create")
def _group_create(Group: GroupSchema, session: Session = Depends(get_session)):
    try:
        return group_service.create_group(Group)
    except:
        return HTTPException(404, "An exception occurred")


def _group_edit(Group: GroupSchema, session: Session = Depends(get_session)):
    try:
        return group_service.edit_group(Group, session)
    except:
        return HTTPException(404, "An exception occurred")


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.2', port=8080)
    # user = User()
    # user.userName = 'This is test User'
    # user.email = 'dingjonghan@gmail.com'
    # user.firstName = 'Le'
    # user.lastName = 'Ming'
    # user.id = uuid.uuid1()
    # session = Session()
    # session.add(user)
    # session = Session()
    # try:
    #     result = session.query(models.User).filter(models.User.id == 'AE5CE941-DC01-11').options(lazyload(models.User.createdGroup)).first()
    #     #result = models.User.query.first()
    #     # group = Group(id= uuid.uuid4(), groupName = "Test Group thui", creator = result)
    #     # session.add(group)
    #     # session.commit()
    #     # group = models.Group(id= uuid.uuid4(), groupName = "Test Group thui", creator = result, createdTime = datetime.now())
    #     #group.createdTime = datetime.now()
    #     session.add(group)
    #     session.commit()
    # finally:
    #     session.close()
    # session.commit()
    # for i in result:
    # i = result
    # print(i.id+" "+ i.userName)
