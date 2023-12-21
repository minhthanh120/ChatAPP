from database.models import User, Session
from fastapi import Depends
from main import get_session


class UserRepository:
    def __init__(self):
        self.session: Session = get_session().__next__()

    def create(self, user):
        newUser = User()
        newUser.id = user.id
        newUser.email = user.email
        newUser.userName = user.userName
        self.session.add(newUser)
        self.session.commit()

    def edit(self, user:User):
        currentUser:User = self.session.query(User).get(user.id)
        currentUser.avatar = user.avatar
        currentUser.firstName = user.firstName
        currentUser.lastName = user.lastName
        currentUser.phone = user.phone
        currentUser.userName = user.userName
        self.session.commit()
        
    def read(self, id:str):
        user =self.session.query(User).get(id)
        return user

    def searchbyEmail(self, email: str):
        return self.session.query(User).filter(User.email.like('%'+email+'%')).all()

    def delete(self, id):
        pass

user_repo = UserRepository()