import uuid
from fastapi import APIRouter, HTTPException, status,Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


from schemas.auth_schema import UserRegister,AuthCustomResponse
from models.db import get_read_session
from models import User
from utils.auth import verify_password,create_access_token,create_refresh_token


user_login_router =APIRouter(tags=["auth"])

""" user register """
@user_login_router.post("/",
    response_model=AuthCustomResponse, 
    status_code=status.HTTP_200_OK, 
    summary="Register User"
)
async def login(payload: UserRegister,session:AsyncSession = Depends(get_read_session)):
    email = payload.email
    check_email = await session.execute(select(User).where(User.email == email))
    user = check_email.scalar_one_or_none()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="user or password is incorrect."
        )
    hash_pass=user.password
    is_password_true = verify_password(payload.password,hash_pass)
    if is_password_true is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="user or password is incorrect."
        )
    access_token = create_refresh_token({"id":user.id,"role":user.role})
    refresh_token = create_refresh_token({"id":user.id,"role":user.role})
    return {
       "id":user.id,
       "email":user.email,
       "role":user.role,
       "username":user.username,
       "access_token" :access_token,
       "refresh_token":refresh_token,
       "createdAt": user.createdAt,
        "updatedAt": user.updatedAt
    }

  
    

