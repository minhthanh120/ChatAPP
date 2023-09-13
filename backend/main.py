
from database.models import Session

from fastapi import FastAPI, HTTPException, Depends, Response
from api.api_v1 import router
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECURITY_ALGORITHM = 'HS256'
SECRET_KEY = '123456'

def get_session():
    session = Session()
    try:
        yield session
    except Exception:
        session.rollback()
    finally:
        session.close()

@app.get("/")
def read_is_first():
    return "Hello"
HOST = '127.0.0.1'
PORT = 8089
if __name__ == '__main__':
    app.include_router(router=router.router)
    uvicorn.run(app, host=HOST, port=PORT)
