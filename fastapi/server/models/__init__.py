from sqlalchemy import (
                        Column, 
                        Integer, 
                        String, 
                        Float, 
                        Text,
                        ForeignKey,
                        func,
                        UniqueConstraint,
                        DateTime
                        )
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from datetime import timezone
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
    createdAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), default=datetime.datetime.now(timezone.utc))
    updatedAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), default=datetime.datetime.now(timezone.utc), onupdate=datetime.datetime.now(timezone.utc))


class Inventory(Base):
    __tablename__ = "esm_inventory"
    id:Mapped[str] = mapped_column(Text,primary_key=True)
    name:Mapped[str] = mapped_column(Text,nullable=False)
    model_no:Mapped[str] = mapped_column(String,nullable=False, unique=True)
    price:Mapped[float] = mapped_column(Float,nullable=True,default=0)
    qty:Mapped[int] = mapped_column(Integer,nullable=True,default=0)
    createdAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), default=datetime.datetime.now(timezone.utc))
    updatedAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), default=datetime.datetime.now(timezone.utc), onupdate=datetime.datetime.now(timezone.utc))