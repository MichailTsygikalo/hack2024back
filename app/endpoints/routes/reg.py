from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from app.endpoints.schema import UserReg
from app.src.utils import hash_password
from app.core.source import check_user_exists, create_new_user
from app.config import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
router = APIRouter()

@router.post('/')
def registr(user: UserReg):

    existing_user = check_user_exists(user.username)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пользователь с таким именем или email уже существует"
        )

    hashed_password = hash_password(user.pswd)

    new_user = create_new_user(user.username, hashed_password)

    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": f"Пользователь успешно зарегистрирован {new_user}"})