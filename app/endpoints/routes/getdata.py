from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from app.endpoints.schema import PasportModel, User, PeopleModel, DocModel, RegistrationModel, ContractorModel
from app.src.utils import get_current_active_user
from app.core.source import *
from app.core.schemas import People, Doc, Pasport, Contractor, Registration
router = APIRouter()

@router.post('/pspt')
def set_pspt(pasport:PasportModel,user:User = Depends(get_current_active_user)):
    
    if not user:
        return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content="Неавторизованный пользователь")
    
    pasport_new = set_passport_db(pasport, user)

    if type(pasport_new) == Pasport:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content="")
    
    return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content=f"{pasport_new}")
    
@router.post('/people')    
def set_people(people:PeopleModel,user:User = Depends(get_current_active_user)):
    if not user:
        return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content="Неавторизованный пользователь")
    
    people_new = set_people_db(people, user)

    if type(people_new) == People:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content="")
    
    return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content=f"{people_new}")

@router.post('/doc')    
def set_docs(docs:DocModel,user:User = Depends(get_current_active_user)):
    
    if not user:
        return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content="Неавторизованный пользователь")
    
    new_doc = set_docs_db(docs, user)

    if type(new_doc) == Doc:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content="")
    
    return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content=f"{new_doc}")

@router.post('/registration/people')    
def set_reg(reg:RegistrationModel,user:User = Depends(get_current_active_user)):
    
    if not user:
        return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content="Неавторизованный пользователь")
    
    new_reg = set_reg_people_db(reg, user)

    if type(new_reg) == Registration:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content="")
    
    return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content=f"{new_reg}")

@router.post('/registration/contractor')    
def set_reg(reg:RegistrationModel,user:User = Depends(get_current_active_user)):
    
    if not user:
        return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content="Неавторизованный пользователь")
    
    new_reg = set_reg_contr_db(reg, user)

    if type(new_reg) == Registration:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content="")
    
    return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content=f"{new_reg}")

@router.post('/contractor')    
def set_con(contractor:ContractorModel,user:User = Depends(get_current_active_user)):
    
    if not user:
        return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content="Неавторизованный пользователь")
    
    new_contractor = set_contractor_db(contractor, user)

    if type(new_contractor) == Contractor:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content="")
    
    return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content=f"{new_contractor}")


@router.get('/pspt')
def get_pspt(user:User = Depends(get_current_active_user)):
    if not user:
        return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content="Неавторизованный пользователь")
    
    pasport_new = get_passport_db(user)

    if type(pasport_new) == Pasport:
        return pasport_new
    
    return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content=pasport_new)


@router.get('/people')    
def get_people(user:User = Depends(get_current_active_user)):
    if not user:
        return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content="Неавторизованный пользователь")
    
    people_new = get_people_db(user)

    if type(people_new) == People:
        return people_new
    
    return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content=f"{people_new}")


@router.get('/doc')    
def get_people(user:User = Depends(get_current_active_user)):
    if not user:
        return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content="Неавторизованный пользователь")
    
    doc_new = get_doc_db(user)

    if type(doc_new) == Doc:
        return doc_new
    
    return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content=f"{doc_new}")



@router.get('/registration/people')    
def get_reg(user:User = Depends(get_current_active_user)):
    
    if not user:
        return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content="Неавторизованный пользователь")
    
    reg_new = get_reg_db(user)

    if type(reg_new) == Registration:
        return reg_new
    
    return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content=f"{reg_new}")


@router.get('/registration/contractor')    
def set_reg(user:User = Depends(get_current_active_user)):
    
    if not user:
        return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content="Неавторизованный пользователь")
    
    reg_new = get_reg_contract_db(user)

    if type(reg_new) == Registration:
        return reg_new
    
    return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content=f"{reg_new}")

@router.get('/contractor')    
def set_con(user:User = Depends(get_current_active_user)):
    
    if not user:
        return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content="Неавторизованный пользователь")
    
    new_contractor = get_contractor_db(user)

    if type(new_contractor) == Contractor:
        return new_contractor
    
    return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content=f"{new_contractor}")
# 12