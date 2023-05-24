from fastapi import APIRouter,
@app.post("/login")
def login(login: Login, session: Session = Depends(get_session)):
    try:
        return authenticate_repository.login(login, session)
    except():
       return HTTPException(404, "An exception occurred")


@app.post("/register")
def register(register: Register, session: Session = Depends(get_session)):
    try:
        return authenticate_repository.register(register, session)
    except:
        return HTTPException(404, "An exception occurred")