from pydantic import BaseModel

class Dummy(BaseModel):
    id: str
    name: str
    description: str | None = None