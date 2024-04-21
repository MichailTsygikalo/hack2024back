from fastapi import APIRouter
from app.endpoints.routes.auth import router as auth_router
from app.endpoints.routes.reg import router as reg_router
from app.endpoints.routes.getdata import router as getdata_router
from app.endpoints.routes.appoinvent import router as appoinvent
from app.endpoints.routes.sales import router as sales

router = APIRouter()

router.include_router(reg_router, tags=['Регистрация'], prefix='/reg')
router.include_router(auth_router, tags=['Авторизация'], prefix='')
router.include_router(getdata_router, tags=['Основная информация'], prefix='/data')
router.include_router(appoinvent, tags=['Бронь(запись на прием)'], prefix='/appoinvent')
router.include_router(sales, tags=['Покупка'], prefix='/buy')

