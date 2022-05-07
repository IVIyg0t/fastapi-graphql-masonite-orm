from typing import Optional

from fastapi import APIRouter, Depends

from models.api.User import UserModel
from models.db.User import User
from src.common import get_password_hash
from src.middleware import get_current_active_user

router = APIRouter(prefix="/users", tags=["users"])


@router.get("")
def get_users(user: UserModel = Depends(get_current_active_user)):
    return User.all().serialize()


@router.post("/user")
def create_user(
    firstname: str,
    lastname: str,
    username: str,
    email: str,
    password: str,
    company_id: int,
    user: UserModel = Depends(get_current_active_user),
):
    user = User.create(
        firstname=firstname,
        lastname=lastname,
        username=username,
        email=email,
        password=get_password_hash(password),
        disabled=False,
        company_id=company_id,
    )

    return user.id


@router.get("/user/me")
def me(user: UserModel = Depends(get_current_active_user)):
    return user.serialize()


@router.put("/user/{id}")
def update_user(
    id: int,
    firstname: Optional[str] = None,
    lastname: Optional[str] = None,
    username: Optional[str] = None,
    email: Optional[str] = None,
    user: UserModel = Depends(get_current_active_user),
):

    user.firstname = firstname or user.firstname
    user.lastname = lastname or user.lastname
    user.username = username or user.username
    user.email = email or user.email

    user.save()

    return user.serialize()


@router.get("/user/{id}")
def get_user(
    id: int,
    user: UserModel = Depends(get_current_active_user),
):
    return User.find_or_fail(id).serialize()


@router.get("/user/{id}/posts")
def get_user_posts(
    id: int,
    user: UserModel = Depends(get_current_active_user),
):
    return User.find_or_fail(id).posts.serialize()
