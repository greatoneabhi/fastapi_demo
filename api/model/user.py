from pydantic import BaseModel, Field


class User(BaseModel):
    id: str = Field(
        None, alias="_id", description="user id", example="65d09e684d3c3a7e81da1be9"
    )
    username: str = Field(
        ..., alias="username", description="user name", example="John123"
    )
    password: str = Field(
        ..., alias="password", description="user password", example="XXXXXXXX"
    )
    email: str = Field(
        ..., alias="email", description="user email", example="john@gmail.com"
    )
    first_name: str = Field(
        ..., alias="firstName", description="user first name", example="John"
    )
    last_name: str = Field(
        ..., alias="lastName", description="user last name", example="Cena"
    )

    class Config:
        populate_by_name = True
        schema_extra = {
            "example": {
                "username": "XXXXXXXX",
                "password": "XXXXXXXX",
                "email": "XXXXXXXX",
                "firstName": "XXXXXXXX",
                "lastName": "XXXXXXXX",
                "_id": "XXXXXXXX",
            }
        }
