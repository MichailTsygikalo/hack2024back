from typing import Optional
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.core.db import Session, get_session
from app.core.schemas import *

def check_user_exists(login)->Optional[User]:
    for session in get_session():
        user = session.execute(select(User).filter(User.login == login)).scalars().first()
    return user

def create_new_user(login, pswd)->Optional[User]:
    
    user = User(
        login = login,
        pswd = pswd,
        status = False
    )
    for session in get_session():
        try:
            session.add(user)
            session.commit()
            return user
        except IntegrityError as e:
            session.rollback()
            return {"IntegrityError:":e}
    
def get_user(login):
    for session in get_session():
        user = session.execute(select(User).filter(User.login == login)).scalars().first()
        user_db = {
            user.login : {
                "username" : user.login,
                "full_name" : user.login,
                "email" : user.login,
                "hashed_password" : user.pswd,
                "disabled" : user.status
            }
        }
    return user_db

def set_passport(pasport, user):
    for session in get_session():
        pass

