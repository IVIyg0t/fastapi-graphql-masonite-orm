import os
from datetime import timedelta
from http.client import HTTPException

from dotenv import load_dotenv
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from models.api.Token import Token
from src.common import authenticate_user, create_access_token

load_dotenv()

router = APIRouter(prefix="/token")


@router.post("", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):

    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
