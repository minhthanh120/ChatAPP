from sqlalchemy.orm import lazyload, joinedload

from database.models import Group, Session, JoinedMember, User, Message
from database.schemas import GroupSchema
from main import get_session
from repositories.member_repository import member_repo


class GroupRepository:
    def __init__(self):
        self.session: Session = get_session().__next__()
    def create(self, group:GroupSchema):
        newGroup = Group()
        newGroup.groupName = group.groupName
        newGroup.creatorId = group.creatorId
        self.session.add(newGroup)
        self.session.commit()
        return newGroup
    def edit(self, group):
        currentGroup = self.read(group.id)
        currentGroup.groupName = group.groupName
        self.session.commit()
        return 'Edit group success'
    def rename(self, id:str, groupName:str):
        currentGroup = self.read(group.id)
        currentGroup.groupName = group.groupName
        self.session.commit()
        return 'Edit group success'
    def read(self, id, getmember=False, getmessages=False):
        currentGroup:Group = self.session.query(Group)\
            .options(
            joinedload(Group.joined)
            .subqueryload(JoinedMember.member)
        ).options(
            joinedload(Group.messages)
        ).get(id)

        return currentGroup
    def delete(self, id):
        currentGroup = self.session.get(Group, id)
        self.session.delete(currentGroup)

    def get_recent(self, userId):
        recent = self.session.query(Group).filter(Group.joined.any(JoinedMember.memberId==userId)).all()
        for group in recent:
            messages = [self.session.query(Message)\
                .filter(Message.groupId == group.id)\
                .order_by(Message.createdTime.desc())\
                .first()]
            group.messages = messages
        #recent = sorted(recent, key = lambda x:(x is None, x.messages[0].createdTime))
        return recent

group_repo = GroupRepository()