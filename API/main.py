from Database.models import engine, User, Login, Register, Group
import uuid
from sqlalchemy.orm import sessionmaker
from typing import Union
from fastapi import FastAPI
from Services import user_service, authorize_service, group_service
import uvicorn
from datetime import datetime
from Database import schemas as base
app = FastAPI()
Session = sessionmaker(bind=engine)

@app.get("/")
def read_foot():
    return {"Hello":"Hello"}
@app.get("/User/{id}")
def read_user(id:int, q:Union[str] = None):
    return {"id":id,"q":q}
@app.post("/login")
def login(login:Login):
    return authorize_service.login(login)
@app.post("/register")
def register(register:Register):
    return authorize_service.register(register)
@app.post("/group_create")
def _group_create(Group:base.Group):
    return 'ok'
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8080)
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
    #     result = session.get(User, 'AE5CE941-DC01-11')
    #     # group = Group(id= uuid.uuid4(), groupName = "Test Group thui", creator = result)
    #     # session.add(group)
    #     # session.commit()
    #     group = Group(id= uuid.uuid4(), groupName = "Test Group thui", creator = result, createdTime = datetime.now())
    #     #group.createdTime = datetime.now()
    #     session.add(group)
    #     session.commit()
    # finally:
    #     session.close()
    # session.commit()
    #for i in result:
    # i = result
    # print(i.id+" "+ i.userName)