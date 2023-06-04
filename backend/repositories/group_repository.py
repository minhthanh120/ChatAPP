from database.models import Group, Session
from database.schemas import GroupSchema
from main import get_session


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
        currentGroup = group
        self.session.commit()
        pass
    def read(id, session):
        return session.query(Group).get(id)
    def delete(group, session):
        pass

group_repo = GroupRepository()