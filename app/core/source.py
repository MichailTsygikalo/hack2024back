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

def set_passport_db(pasport, user):
    for session in get_session():
        user_id = session.execute(select(User).where(User.login == user.username)).scalars().first().id
        pasport_add = Pasport(
            series = pasport.series, 
            number = pasport.number, 
            data_issue = pasport.data_issue
        )

def set_people_db(people, user):
    for session in get_session():
        user_id = session.execute(select(User).where(User.login == user.username)).scalars().first().id
        people_add = People(
                surname = people.surname, 
                name = people.name, 
                sec_name = people.sec_name, 
                birthday = people.birthday, 
                user_id = user_id
            )
        try:
            session.add(people_add)
            session.commit()
            return people_add
        except IntegrityError as e:
            session.rollback()
            return e
    
