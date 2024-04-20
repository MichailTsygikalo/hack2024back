from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from app.endpoints.schema import PasportModel, User, PeopleModel, DocModel, RegistrationModel, ContractorModel
from app.src.utils import get_current_active_user
from app.core.source import set_people_db, set_passport_db
from app.core.schemas import People
router = APIRouter()

@router.post('/pspt')
def set_pspt(pasport:PasportModel,user:User = Depends(get_current_active_user)):
    
    if not user:
        return {'message':'неавторизованный пользователь'}
    
    pasport_new = set_passport_db(pasport, user)

    if pasport_new:
        return JSONResponse(status_code=status.HTTP_201_CREATED)
    
    return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY)
    
@router.post('/people')    
def set_people(people:PeopleModel,user:User = Depends(get_current_active_user)):
    if not user:
        return {'message':'неавторизованный пользователь'}
    
    people_new = set_people_db(people, user)

    if type(people_new) == People:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content="")
    
    return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content=f"{people_new}")

@router.post('/doc')    
def set_docs(docs:DocModel,user:User = Depends(get_current_active_user)):
    
    if not user:
        return {'message':'неавторизованный пользователь'}

@router.post('/registration')    
def set_reg(reg:RegistrationModel,user:User = Depends(get_current_active_user)):
    
    if not user:
        return {'message':'неавторизованный пользователь'}

    

@router.post('/contractor')    
def set_con(contractor:ContractorModel,user:User = Depends(get_current_active_user)):
    
    if not user:
        return {'message':'неавторизованный пользователь'}