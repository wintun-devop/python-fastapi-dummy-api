from pydantic import BaseModel
from datetime import datetime


class InventoryCreate(BaseModel):
    name:str
    model_no:str
    price:float
    qty:int

class InventoryRead(InventoryCreate):
    id:str
    createdAt: datetime
    updatedAt: datetime | None

    class Config:
        from_attributes = True
   