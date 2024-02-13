from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# start the server : uvicorn users:router --reload

# User entity
class User(BaseModel):
    id: int
    name: str
    surname: str
    favouriteMeal: str
    age: int

users_list=[User(1,"Rodrigo","López Soria","Pizza",30),
       User(2,"Laura","Gonzalez","Pizza",30),
       User(3,"Patrick","Mescal","Pizza",30)
       ]


@router.get("/usersjson")
async def usersJson():
    return User(id= 1, name="Rodrigo", surname="López Soria", favouriteMeal= "Pizza", age= 30)

@router.get("/users")
async def users():
    return users_list

@router.get("/user/{id}")
async def user(id: int):
    user = filter(lambda user:user.id==id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"User not found"}
    
@router.get("/userquery/")
async def user(id: int):
    user = filter(lambda user:user.id==id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"User not found"}

@router.post("/new_user/")
async def create_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(satus_code=404, detail="User already exists") 
    else:
        users_list.routerend(user)
        return user


def search_user(id: int):
    user = filter(lambda user:user.id==id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"User not found"}
    
@router.put("/edit_user/")
async def user(user: User):

    found= False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error":"User not found"}
    
    return user

@router.delete("/delete_user/{id}")
async def delete_user(id: int):
       for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            


