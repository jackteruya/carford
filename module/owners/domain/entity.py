from datetime import date

from pydantic import BaseModel


class Owner(BaseModel):
    id: int
    name: str
    document: str
    date_of_birth: date
