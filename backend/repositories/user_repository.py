from database.models import User, Session


def create(user, session):
    session.add(user)
    session.commit()
def edit(user, session):
    pass
def read(id, session: Session):
    return session.query(User).get(id)

def searchbyemail(email:str, session: Session):
    return session.query(User).filter(User.email.like('%'+email+'%')).all()
def delete(id, session):
    pass
