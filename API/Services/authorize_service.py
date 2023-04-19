from Database.models import Login, Register, Session
from Repositories import authenticate_repository
def login(Login):
    return authenticate_repository.authenticate(Login)
    
def register(Register):
    pass
def log_out():
    pass