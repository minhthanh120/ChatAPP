from database.models import Message, Session, JoinedMember, Group
from datetime import datetime
from sqlalchemy import  select, func
from sqlalchemy import desc
from sqlalchemy.sql.functions import coalesce
import json
from main import get_session


class MessageRepository:
    def __init__(self):
        self.session: Session = get_session().__next__()
    def create(self, message:Message):
        self.session.add(message)
        self.session.commit()
        return 'Sent Message!'
    def edit(self, message):
        currentMessage:Message = self.read(message.id)
        currentMessage.content = message.content
        self.session.commit()
        return 'Edited Message!'
    def read(self, id):
        return self.session.query(Message).get(id)
    def delete(self, id):
        currentMessage = self.session.query(Message).get(id)
        self.session.delete(currentMessage)
        self.session.commit()
        return 'Deleted Message!'
    def recentMessage(self, userId):
        # List group that user joined
        lstGrp = self.session.query(Group.id, Group.groupName, Group.createdTime).join(JoinedMember,
            Group.id == JoinedMember.groupId).distinct(JoinedMember.groupId).filter(JoinedMember.memberId == '3622BBFB-EE0A-47').subquery()
        # Get most lastest message in each group
        subquery = self.session.query(func.rank().over(order_by=Message.createdTime.desc(), partition_by=Message.groupId).label('rnk'),
            Message.id, Message.content, Message.groupId, Message.senderId, Message.createdTime
        ).subquery()
        # Query the top-ranked message from each group
        query = self.session.query(lstGrp, subquery).outerjoin(
            subquery, lstGrp.c.id == subquery.c.groupId, full=True).order_by(
            coalesce(subquery.c.createdTime, lstGrp.c.createdTime).desc()).filter(
            (subquery.c.rnk == 1)| (subquery.c.rnk == None)).all()
        return [list(row) for row in query]        
message_repo = MessageRepository()