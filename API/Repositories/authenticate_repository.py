from Database.models import UserAuth, Session
from Database.schemas import Login

def create(session):
    pass
def edit(session):
    pass
def read(session):
    pass
def delete(session):
    pass

def authenticate(Login:Login):
    session = Session()
    try:
        #isUser = session.query(UserAuth).filter_by(userName = Login.userName, hashedPassword.encriptedValue = Login.password).first() is not None
        a = 'ok'
    finally:
        session.close()
    return isUser

# change user password
