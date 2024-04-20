from passlib.context import CryptContext
from app.core.source import get_user
from app.endpoints.schema import User, Token, TokenData, UserInDB
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from typing import Annotated
from fastapi import APIRouter, Depends, FastAPI, HTTPException, status

from datetime import datetime, timedelta, timezone
from app.config import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
 

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str):
    user = get_user(username)
    user_dict = get_user_dict(user,username )
    
    if not user:
        return False
    if not verify_password(password, user[username]["hashed_password"]):
        return False
    return user_dict

def get_user_dict(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(login=token_data.username)
    user_dict = get_user_dict(user,token_data.username )
    if user is None:
        raise credentials_exception
    return user_dict

def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if not current_user:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user