from database.models import JoinedMember, Session, User
from main import get_session
from sqlalchemy.orm import lazyload, joinedload

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
    def get_all_by_groupId(self, groupId:str):
        result = self.session.query(JoinedMember)\
            .options(joinedload(JoinedMember.member))\
            .filter(JoinedMember.groupId == groupId)\
            .all()
        return result
    def delete(self, groupId:str, memberId:str):
        current = self.session.query(JoinedMember).filter(JoinedMember.groupId == groupId
                                                          and JoinedMember.memberId == memberId).first()
        return "OK"
    def isMember(self, groupId, userId):
        member: JoinedMember = self.session.query(JoinedMember).filter(
            JoinedMember.memberId == userId, JoinedMember.groupId == groupId).first()
        return member != None
    def isAdmin(self, groupId, userId):
        admin:JoinedMember = self.session.query(JoinedMember)\
            .filter(JoinedMember.memberId==userId, JoinedMember.groupId==groupId,
                    JoinedMember.role!=None).first()
        return admin != None
    def userNotInGroup(self, groupId, key):
        memmbers = self.session.query(JoinedMember.memberId).filter(
            JoinedMember.groupId == groupId  ).subquery()
        not_joined = self.session.query(User).filter(User.id.not_in(memmbers)
                                                     and User.userName.contains(key)).all()
        return not_joined

member_repo = MemberRepository()