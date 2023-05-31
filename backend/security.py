import jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from database.models import User, Session
from database.schemas import TokenData
from setting import setting
from  pydantic import ValidationError
from datetime import datetime
from repositories.user_repository import user_repo as user_repository


reuasble_oauth2 = OAuth2PasswordBearer(
    tokenUrl= "login",
    scheme_name='Authorization'
)

def get_current_user(token:str = Depends(reuasble_oauth2))->User:
    try:
        payload = jwt.decode(
            token, setting.JWT_SECRET_KEY, algorithms=[setting.ALGORITHM]
        )
        tokenData = TokenData(**payload)
    except(jwt.PyJWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate":"Bearer"}
        )
    user = user_repository.read(tokenData.sub)
    return user