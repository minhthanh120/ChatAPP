from sqlalchemy.orm import joinedload

from database.models import Group, User, Session, JoinedMember

session:Session = Session()
g1 = session.get(Group, 'E4B262D9-B49D-43DF-819B-E31C0BE73477')
g2 = session.query(Group).get('E4B262D9-B49D-43DF-819B-E31C0BE73477')
group = session.query(Group).options(joinedload(Group.joined)).filter_by(id='E4B262D9-B49D-43DF-819B-E31C0BE73477').first()



user = session.get(User, '7001034d-db82-11ed-a300-70a6ccc4b566')
