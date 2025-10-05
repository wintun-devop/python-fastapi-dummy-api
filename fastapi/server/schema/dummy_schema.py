from pydantic import BaseModel
from typing import Optional

class Dummy(BaseModel):
    id: str
    name: str
    description: str | None = None

class DummyUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None