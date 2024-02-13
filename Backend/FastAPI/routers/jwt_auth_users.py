from fastapi import APIRouter, Depends,HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM= "HS256"
ACCESS_TOKEN_DURATION=1
SECRET="lrdgjlgnjrlgnkvn3456mrlejtoingjldfnkbkdnkdngkdfnglkjfgkj"

router= APIRouter()

oauth2= OAuth2PasswordBearer(tokenUrl="login")

crypt= CryptContext(schemes=["bcrypt"])


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


    

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HHTP_401_UNAUTHORIZED, 
                            detail="Incorrect user", 
                            headers={"WWW-Authenticate":"Bearer"})
    
    user = find_user(form.username)

    
    if not crypt.verify(form.passsword, user.password):
                raise HTTPException(
                     status_code=400, detail="Incorrect password")

    access_token = {"sub":user.username, "exp":datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}


    return {"access_token": jwt.encode(access_token, algorithm=ALGORITHM), "token_type": "bearer"}

@router.get("/users/me")
async def me(user: User = Depends()):
     return user

def find_user(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
async def auth_user(token: str = Depends(oauth2)):

    exception = HTTPException(
               status_code=status.HTTP_401_UNAUTHORIZED,
               detail="Incorrect credentials", 
               headers={"WWW-Authenticate":"Bearer"})
    
    try:
        user = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if user is None:
             raise exception

        return find_user(user)    

             
    except JWTError:
         raise exception
    
async def current_user(user: User = Depends(auth_user())):
     if user.disabled:
          raise HTTPException(
               status_code=status.HTTP_400_BAD_REQUEST,
               detail="Disabled user", 
               headers={"WWW-Authenticate":"Bearer"})
     return user
          
     
          
