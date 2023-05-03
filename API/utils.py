from pathlib.context import CryptContext
password_context = CryptContext(schemes=['bcrypt'], deprecated ="auto")

def get_hashed_password(password:str) -> str:
    return password_context.hash(password)
def verify_password(password:str, hashed_pass:str)-> bool:
    return password_context.verify(password, hashed_pass)
def on_success(data = None, message = 'success'):
    if data is not None:
        return data, message
    else:
        on_fail()
def on_fail(message:'failed'):
    return message
def send_file():
    pass
