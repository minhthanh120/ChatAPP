from passlib.context import CryptContext
import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt
password_context = CryptContext(schemes=['bcrypt'], deprecated ="auto")
from setting import setting

def create_access_token(data: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(data)}
    encoded_jwt = jwt.encode(to_encode, setting.JWT_SECRET_KEY, setting.ALGORITHM)
    return encoded_jwt

def create_refresh_token(data: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=setting.REFRESH_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(data)}
    encoded_jwt = jwt.encode(to_encode, setting.JWT_REFRESH_SECRET_KEY, setting.ALGORITHM)
    return encoded_jwt

def get_hashed_password(password:str) -> str:
    return password_context.hash(password)
def verify_password(password:str, hashed_pass:str)-> bool:
    return password_context.verify(password, hashed_pass)

if __name__ =='__main__':
    print(get_hashed_password("password"))