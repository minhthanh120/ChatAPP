from fastapi.security import OAuth2PasswordBearer
reuasble_oauth2 = OAuth2PasswordBearer(
    tokenUrl= "http://127.0.0.2:8080/login",
    scheme_name='Authorization'
)