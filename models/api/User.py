from typing import Optional

from models.api.Base import BaseModel


class UserModel(BaseModel):
    firstname: str
    lastname: str
    username: str
    email: str | None = None
    password: str | None = None
    disabled: str | None = None
    company_id: int | None = None


class UserInDB(UserModel):
    hashed_password: str
