from pydantic import BaseModel
from typing import Optional

employees = {
    1: {
        "name": "Michael",
        "age": 45,
        "pos": "Manager"
    }
}


class NewEmployee(BaseModel):
    name: str
    age: int
    pos: str


class UpdateEmployee(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    pos: Optional[str] = None