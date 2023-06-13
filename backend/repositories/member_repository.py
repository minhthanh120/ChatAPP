from database.models import JoinedMember, Session
from main import get_session
class MemberRepository:
    def __init__(self):
        self.session: Session = get_session().__next__()
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
    def isMember(self, groupId, userId):
        member: JoinedMember = self.session.query(JoinedMember).filter(
            JoinedMember.memberId == userId, JoinedMember.groupId == groupId).first()
        return member != None
    def isAdmin(self, groupId, userId):
        admin:JoinedMember = self.session.query(JoinedMember).filter(JoinedMember.memberId==userId, JoinedMember.groupId==groupId, JoinedMember.role!=None).first()
        return admin != None

member_repo = MemberRepository()