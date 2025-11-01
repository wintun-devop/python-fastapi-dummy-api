import uuid
from fastapi import APIRouter, HTTPException, status,Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession


from schemas.auth_schema import UserRegister,AuthCustomResponse
from models.db import get_write_session
from models import User
from utils.auth import hashed_password


user_register_router =APIRouter(tags=["auth"])


""" user register """
@user_register_router.post("/",
    response_model=AuthCustomResponse, 
    status_code=status.HTTP_201_CREATED, 
    summary="Register User"
)
async def create_item(payload: UserRegister,session:AsyncSession = Depends(get_write_session)):
        new_user = User(
        id=str(uuid.uuid4()),
        # or payload.username if you add it to the schema
        username=payload.email.split("@")[0],  
        email=payload.email,
        # → in prod, hash this!
        password=hashed_password(payload.password), 
         )
        try:
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            return new_user
        except IntegrityError:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email or username already registered"
            )

