from fastapi import APIRouter, Depends,HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


router= APIRouter()

oauth2= OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db={
    "rodrigolsoria":{
        "username": "rodrigolsoria",
        "full_name": "Rodrigo López Soria",
        "email": "rodrigolopezsoria@gmail.com",
        "disabled": False,
        "password": "webdev100"
    },
    "rodrigolsoria2":{
        "username": "rodrigolsoria2",
        "full_name": "Rodrigo López Soria ",
        "email": "rodrigolopezsoria2@gmail.com",
        "disabled": True,
        "password": "fastapirules!"
    },
}

def find_user(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
async def current_user(token: str = Depends(oauth2)):
     user= find_user(token)
     if not user:
          raise HTTPException(
               status_code=status.HTTP_401_UNAUTHORIZED,
               detail="Incorrect credentials", 
               headers={"WWW-Authenticate":"Bearer"})
          


    
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HHTP_401_UNAUTHORIZED, 
                            detail="Incorrect user", 
                            headers={"WWW-Authenticate":"Bearer"})
    
    user = find_user(form.username)
    if form.password == user.password:
                raise HTTPException(
                     status_code=400, detail="Incorrect password")
    return {"access_token": user.username, "token_type": "bearer"}

@router.get("/users/me")
async def me(user: User = Depends()):
     return user