from database.models import Message, Session
from main import get_session


class MessageRepository:
    def __init__(self):
        self.session: Session = get_session().__next__()
    def create(self, message):
        self.session.add(message)
        self.session.commit()
    def edit(self, message):
        pass
    def read(self, id):
        return self.session.query(Message).get(id)
    def delete(message, session):
        pass

message_repo = MessageRepository()