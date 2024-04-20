from typing import Optional
from sqlalchemy import select, update
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
        people_id = session.execute(select(People).where(People.user_id == user_id)).scalars().first().id
        pasport_add = Pasport(
            series = pasport.series, 
            number = pasport.number, 
            date_issue = pasport.date_issue,
            people_id = people_id
        )
        try:
            session.add(pasport_add)
            session.commit()
            return pasport_add
        except IntegrityError as e:
            session.rollback()
            return e

def set_people_db(people, user):
    for session in get_session():
        user_id = session.execute(select(User).where(User.login == user.username)).scalars().first().id
        people_add = People(
                surname = people.surname, 
                name = people.name, 
                sec_name = people.sec_name, 
                birthday = people.birthday, 
                user_id = user_id,
            )
        try:
            session.add(people_add)
            session.commit()
            return people_add
        except IntegrityError as e:
            session.rollback()
            return e
    
def set_docs_db(docs, user):
    for session in get_session():
        user_id = session.execute(select(User).where(User.login == user.username)).scalars().first().id
        people_id = session.execute(select(People).where(People.user_id == user_id)).scalars().first().id
        pasport_id = session.execute(select(Pasport).where(Pasport.people_id == people_id)).scalars().first().id
        docs_add = Doc(
            polis = docs.polis,
            snils = docs.snils,
            people_id = people_id,
            pasport_id = pasport_id
        )
        try:
            session.add(docs_add)
            session.commit()
            return docs_add
        except IntegrityError as e:
            session.rollback()
            return e

def set_contractor_db(contractor, user):
    for session in get_session():
        user_id = session.execute(select(User).where(User.login == user.username)).scalars().first().id
        contractor_add = Contractor(
            name = contractor.name,
            user_id = user_id
        )  
        try:
            session.add(contractor_add)
            session.commit()
            return contractor_add
        except IntegrityError as e:
            session.rollback()
            return e  
        
def set_reg_people_db(reg, user):
    for session in get_session():
        user_id = session.execute(select(User).where(User.login == user.username)).scalars().first().id
        people_id = session.execute(select(People).where(People.user_id == user_id)).scalars().first().id
        pasport = session.execute(select(Pasport).where(Pasport.people_id == people_id)).scalars().first()

        new_reg = Registration(
            city = reg.city,
            streat = reg.streat,
            home = reg.home,
            flat = reg.flat,
            x = reg.coord_x,
            y = reg.coord_y
        )
        try:
            session.add(new_reg)
            session.commit()
            new_pasport = session.execute(update(Pasport).values(registration_id = new_reg.id))
            session.commit()
            return new_reg
        except IntegrityError as e:
            session.rollback()
            return e


def set_reg_contr_db(reg, user):
    for session in get_session():
        user_id = session.execute(select(User).where(User.login == user.username)).scalars().first().id
        contractor = session.execute(select(Contractor).where(Contractor.user_id == user_id)).scalars().first()

        new_reg = Registration(
            city = reg.city,
            streat = reg.streat,
            home = reg.home,
            flat = reg.flat,
            x = reg.coord_x,
            y = reg.coord_y
        )
        try:
            session.add(new_reg)
            session.commit()
            new_contractor = session.execute(update(Contractor).values(registration_id = new_reg.id))
            session.commit()
            return new_reg
        except IntegrityError as e:
            session.rollback()
            return e
        
def get_passport_db(user):
    for session in get_session():
        user_id = session.execute(select(User).where(User.login == user.username)).scalars().first().id
        people_id = session.execute(select(People).where(People.user_id == user_id)).scalars().first().id
        pasport_new =  session.execute(select(Pasport).filter(Pasport.people_id == people_id)).scalars().first()
        if pasport_new:
            return pasport_new
    return None

def get_people_db(user):
    for session in get_session():
        user_id = session.execute(select(User).where(User.login == user.username)).scalars().first().id
        people_new = session.execute(select(People).where(People.user_id == user_id)).scalars().first()
        if people_new:
            return people_new
    return None

def get_doc_db(user):
    for session in get_session():
        user_id = session.execute(select(User).where(User.login == user.username)).scalars().first().id
        people_id = session.execute(select(People).where(People.user_id == user_id)).scalars().first().id
        doc_new = session.execute(select(Doc).where(Doc.people_id == people_id)).scalars().first()
        if doc_new:
            return doc_new
    return None

def get_reg_db(user):
    for session in get_session():
        user_id = session.execute(select(User).where(User.login == user.username)).scalars().first().id
        people_id = session.execute(select(People).where(People.user_id == user_id)).scalars().first().id
        pasport_id =  session.execute(select(Pasport).filter(Pasport.people_id == people_id)).scalars().first().id
        reg_new = session.execute(select(Registration).filter(Registration.id == pasport_id)).scalars().first()
        if reg_new: 
            return reg_new
    return None

def get_reg_contract_db(user):
    for session in get_session():
        user_id = session.execute(select(User).where(User.login == user.username)).scalars().first().id
        contractor_id = session.execute(select(Contractor).where(Contractor.user_id == user_id)).scalars().first().id
        reg_new = session.execute(select(Registration).filter(Registration.id == contractor_id)).scalars().first()
        if reg_new:
            return reg_new
    return None

def get_contractor_db(user):
    for session in get_session():
        user_id = session.execute(select(User).where(User.login == user.username)).scalars().first().id
        constract_new =session.execute(select(Contractor).where(Contractor.user_id == user_id)).scalars().first()
        if constract_new:
            return constract_new
    return None