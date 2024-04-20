from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from app.endpoints.schema import PasportModel, User, PeopleModel, DocModel, RegistrationModel, ContractorModel
from app.src.utils import get_current_active_user

router = APIRouter()

@router.post('/pspt')
def set_pspt(pasport:PasportModel,user:User = Depends(get_current_active_user)):
    
    if not user:
        return {'message':'неавторизованный пользователь'}
    
    pasport = set_passport(pasport, user)

    if pasport:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": f"Пользователь успешно зарегистрирован {new_user}"})
    
    return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY)
    
@router.post('/people')    
def set_pspt(people:PeopleModel,user:User = Depends(get_current_active_user)):
    
    if not user:
        return {'message':'неавторизованный пользователь'}

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