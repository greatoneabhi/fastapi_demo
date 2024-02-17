from typing import List
from fastapi import APIRouter, Request, Response
from api.model.user import User

import logging
import json

logger = logging.getLogger(__name__)

user = APIRouter()


@user.post("/users", status_code=201, response_model=User, tags=["user"])
def create_user(request: Request, user: User):
    if user.id is None:
        del user.id
    logger.info(f"create user {user}")
    resutl = request.app.database.users.insert_one(user.model_dump(by_alias=True))
    user.id = str(resutl.inserted_id)
    return Response(content=json.dumps(user.model_dump(by_alias=True)), media_type="application/json")


@user.get("/users", response_model=List[User], tags=["user"])
def get_users(request: Request):
    logger.info(f"get users")
    users = []
    users_from_db: list[User] = request.app.database.users.find()
    for user_db in users_from_db:
        user_db["_id"] = str(user_db["_id"])
        users.append(User(**user_db).model_dump(by_alias=True))
    return Response(content=json.dumps(users), media_type="application/json")




    