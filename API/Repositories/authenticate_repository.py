from Database.models import UserAuth, Login, Session

def authenticate(Login:Login):
    session = Session()
    try:
        #isUser = session.query(UserAuth).filter_by(userName = Login.userName, hashedPassword.encriptedValue = Login.password).first() is not None
        a = 'ok'
    finally:
        session.close()
    return isUser
