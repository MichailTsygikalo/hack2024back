from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from app.endpoints.schema import User as U
from app.src.utils import get_current_active_user

#
from app.core.schemas import Service, Sales, People, User, Contractor
from sqlalchemy.exc import IntegrityError
from app.core.db import get_session
from sqlalchemy import select
#

router = APIRouter()

@router.post('/')
def appoinment(service_id:int, time: str, user:U = Depends(get_current_active_user)):
    if not user:
        return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content="Неавторизованный пользователь")
    
    return {'service':appoinment_db(service_id, time, user)['service'],'time': time}

def appoinment_db(service_id, time, user:U): #регистрация записи
    for session in get_session():
        service = session.execute(select(Service).where(Service.id == service_id)).scalars().first()
        user_id = session.execute(select(User).filter(User.login == user.username)).scalars().first().id
        people = session.execute(select(People).where(People.user_id == user_id)).scalars().first()

        new_sale = Sales(
            people_id = people.id,
            service_id = service.id,
            date = time
        )
        try:
            session.add(new_sale)
            session.commit()
            return {'sale':new_sale, 'service':service}
        except IntegrityError as e:
            session.rollback()
            return {"IntegrityError:":e}