from app.core.db import Session, get_session
from app.core.schemas import *
from sqlalchemy import select, update


def get_service(user, service, contractor):
    print(service, contractor)
    for session in get_session():
        service = session.execute(select(Service).filter(
            Service.contractor_id == contractor,
            Service.id == service
        )).scalars().first()
        
        new_user = session.execute(select(User).filter(
            User.login == user.username
        )).scalars().first()
        if new_user.balance_money-service.price <0:
            return "недостаточно средств"
        user_balance = session.execute(update(User).values(balance_money = (new_user.balance_money - service.price)).where(User.id == new_user.id))
        session.commit()
        people_id = session.execute(select(People).where(People.user_id == new_user.id)).scalars().first().id
        
        sales = Sales(
            people_id = people_id,
            service_id = service.id, 
            sum = service.price, 
            count = 1
        )
        session.add(sales)
        session.commit()
    return sales
