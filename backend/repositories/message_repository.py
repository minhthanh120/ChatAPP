from database.models import Message
def create(message, session):
    session.add(message)
    session.commit()
def edit(message, session):
    pass
def read(id, session):
    return session.query(Message).get(id)
def delete(message, session):
    pass