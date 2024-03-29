from fastapi import APIRouter, HTTPException
from db.models.user import User
from db.client import db_client
from db.schemas import user_schema, users_schema
from bson import ObjectId

router = APIRouter(prefix="/userdb",
                   tags=["userdb"],
                   responses={404:{"message": "Not found"}})

# start the server : uvicorn users:router --reload


users_list=[]



@router.get("/", response_model=list[User])
async def users():
    return users_schema(db_client.users.find())

@router.get("/{id}")
async def user(id: str):
    return search_user("_id", ObjectId(id))
    
@router.get("/") #query
async def user(id: str):
        return search_user("_id", ObjectId(id))


@router.post("/create")
async def create_user(user: User):
    if(type(search_user("email", user.email)) == User):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User already exists"
        )

    user_dict = dict(user)
    del user_dict["id"]

    id = db_client.users.insert_one(user_dict).inserted_id

    new_user = user_schema(db_client.users.find_one({"id":id}))
    return User(**new_user)


def search_user(field: str, key):
    try:
        user= db_client.users.find_one({field:key})
        return User(**user_schema(user))
    except:
        return {"error":"User not found"}
    

@router.put("/edit", response_model=User)
async def user(user: User):
    user_dict = dict(user)
    del user_dict["id"]
    try:
         db_client.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)
    except:
        return {"error": "user not updated"}

    return  search_user("_id", ObjectId(user.id))


      

@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: str):
       
       found= db_client.users.find_one_and_delete({"_id": ObjectId(id)})

       if not found:
            return {"error": "User not deleted"} 
            


