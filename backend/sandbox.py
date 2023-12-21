from sqlalchemy import select, desc, text, func
from fastapi.encoders import jsonable_encoder
from database.models import Session, Group, JoinedMember, User, Message

session = Session()


memmbers = session.query(JoinedMember.memberId).filter(JoinedMember.groupId == 'C106161E-87FE-4F97-B4F0-2C40F2723F68').subquery()
not_joined = session.query(User).filter(User.id.not_in(memmbers)).all()
print(jsonable_encoder(not_joined))