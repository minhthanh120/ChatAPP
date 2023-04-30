from Repositories import message_repository
def send_message(message, session):
    return message_repository.create(message, session)
def delete_message():
    pass
def edit_message():
    pass
def load_message():
    pass
def join_group():
    pass