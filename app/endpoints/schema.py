from datetime import datetime
from pydantic import BaseModel, EmailStr, validator, constr

class UserReg(BaseModel):
    username: EmailStr
    pswd: constr(min_length=8)
    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str


class PasportModel(BaseModel):
    series:str
    number: str
    date_issue: datetime

    class Config:
        arbitrary_types_allowed = True


class PeopleModel(BaseModel):
    surname:str
    name: str
    sec_name: str
    photo: str|None
    birthday: datetime

    class Config:
        arbitrary_types_allowed = True

class DocModel(BaseModel):
    polis: constr(max_length=16)
    snils: constr(max_length=14)

    class Config:
        arbitrary_types_allowed = True

class RegistrationModel(BaseModel):
    city: str
    streat: str
    home: str
    flat: str
    coord_x: str
    coord_y: str

    class Config:
        arbitrary_types_allowed = True

class ContractorModel(BaseModel):
    name:str

    class Config:
        arbitrary_types_allowed = True