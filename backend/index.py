from database.models import Session, Group, JoinedMember, User

session = Session()


def isMember(groupId, userId) -> bool:
    print('1')
    member: JoinedMember = session.query(JoinedMember).filter(
        JoinedMember.memberId == userId, JoinedMember.groupId == groupId).first()
    return member != None


def isAdmin(groupId, userId) -> bool:
    admin: JoinedMember = session.query(JoinedMember).filter(JoinedMember.memberId == userId,
                                                             JoinedMember.groupId == groupId,
                                                             JoinedMember.role != None).first()
    return admin != None


#recent = session.query(Group).filter(Group.joined.any(JoinedMember.memberId == '7001034d-db82-11ed-a300-70a6ccc4b566')).all()
recent = session.query(Group).join(JoinedMember, Group.joined).order_by(JoinedMember.joinedTime.asc()).filter(JoinedMember.groupId == 'E4B262D9-B49D-43DF-819B-E31C0BE73477')\
    .all()
#recent:Group = session.query(Group).filter(Group.id == 'E4B262D9-B49D-43DF-819B-E31C0BE73477').first()
