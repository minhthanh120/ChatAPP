from Database.models import User
def create(user, session):
    session.add(message)
    session.commit()
def edit(user, session):
    pass
def read(id, session):
    return session.query(User).get(id)
def delete(id, session):
    pass
