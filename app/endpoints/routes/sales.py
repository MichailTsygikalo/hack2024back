from fastapi import APIRouter, Depends, status
from app.endpoints.schema import User
from app.src.utils import get_current_active_user
from app.core.sales_query import get_service
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post('/')
def get_sales(service_id: int, contractor_id: int, user:User = Depends(get_current_active_user)):
    print(service_id, contractor_id)
    if user:
        service_cost = get_service(user, service_id, contractor_id)
        return service_cost
    return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY, content="not client")