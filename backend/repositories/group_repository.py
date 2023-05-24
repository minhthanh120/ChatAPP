from database.models import Group
def create(group, session):
    session.add(group)
    session.commit()
    pass
def edit(group, session):
    currentGroup = read(group.id, session)
    currentGroup = group
    session.commit()
    pass
def read(id, session):
    return session.query(Group).get(id)
def delete(group, session):
    pass
