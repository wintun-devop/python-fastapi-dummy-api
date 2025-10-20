from sqlalchemy import (
                        Column, 
                        Integer, 
                        String, 
                        Float, 
                        Text,
                        ForeignKey,
                        func,
                        UniqueConstraint
                        )
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
import datetime

class Base(AsyncAttrs,DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "esm_users"
    id:Mapped[str] = mapped_column(Text,primary_key=True)
    username:Mapped[str] = mapped_column(String,nullable=False,unique=True)
    email:Mapped[str] = mapped_column(String,nullable=False,unique=True)
    password:Mapped[str] = mapped_column(String,nullable=False)
    role:Mapped[str] = mapped_column(String,nullable=True,default="user")
    createdAt: Mapped[datetime.datetime] = mapped_column(default=func.now())
    updatedAt: Mapped[datetime.datetime] = mapped_column(default=func.now(),onupdate=func.now())