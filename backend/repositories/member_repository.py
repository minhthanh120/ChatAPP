from database.models import JoinedMember
from main import get_session
class MemberRepository:
    def __init__(self):
        self.session = get_session().__next__()
    def create(self, groupId, memberId):
        joined = JoinedMember()
        joined.groupId = groupId
        joined.memberId = memberId
        self.session.add(joined)
        self.session.commit()
    def edit(self):
        pass
    def read(self):
        pass
    def delete(self):
        pass

member_repo = MemberRepository()