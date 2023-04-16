from Database.models import engine, User
import uuid
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
if __name__ == '__main__':
    # user = User()
    # user.userName = 'This is test User'
    # user.email = 'dingjonghan@gmail.com'
    # user.firstName = 'Le'
    # user.lastName = 'Ming'
    # user.id = uuid.uuid1()
    # session = Session()
    # session.add(user)
    session = Session()
    try:
        result = session.query(User).get('D0FA2F2F-DBB0-11')
    finally:
        session.close()
    session.commit()
    #for i in result:
    i = result
    print(i.id+" "+ i.userName)