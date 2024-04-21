from fastapi import FastAPI
import uvicorn
from app.endpoints import router

app = FastAPI(title="Карта жителя Ростова")
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run("app.main:app", port=8000, host='0.0.0.0', reload=True)

