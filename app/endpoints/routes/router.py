from fastapi import APIRouter
from app.endpoints.routes.auth import router as auth_router
from app.endpoints.routes.reg import router as reg_router

router = APIRouter()

router.include_router(auth_router, tags=['Авторизация'], prefix='/auth')
router.include_router(reg_router, tags=['Регистрация'], prefix='/reg')

