from datetime import date

from pydantic import BaseModel


class CarCreateRequest(BaseModel):
    name: str
    color: str
    model: str
    owner_id: int
