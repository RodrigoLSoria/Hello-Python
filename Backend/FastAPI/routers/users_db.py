from fastapi import APIRouter, HTTPException
from db.models.user import User
from db.client import db_client
from db.schemas import user_schema

router = APIRouter()

# start the server : uvicorn users:router --reload


users_list=[]



@router.get("/usersdb")
async def users():
    return users_list

@router.get("/userdb/{id}")
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

@router.post("/new_userdb/")
async def create_user(user: User):
    if(type(search_user_by_email(user.email)) == User):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User already exists"
        )

    user_dict = dict(user)
    del user_dict["id"]

    id = db_client.local.users.insert_one(user_dict).inserted_id

    new_user = user_schema(db_client.local.users.find_one({"id":id}))
    return User(**new_user)


def search_user_by_email(email: str):
    try:
        user= db_client.local.users.find_one({"email":email})
        return User(user_schema(**user))
    except:
        return {"error":"User not found"}
    
@router.put("/edit_userdb/")
async def user(user: User):

    found= False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error":"User not found"}
    
    return user

@router.delete("/delete_userdb/{id}")
async def delete_user(id: int):
       for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            


