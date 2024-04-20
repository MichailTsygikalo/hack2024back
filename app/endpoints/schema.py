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