from pydantic import BaseModel

class TableCreate(BaseModel):
    description: str
    status: bool