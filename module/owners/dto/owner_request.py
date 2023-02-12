from datetime import date

from pydantic import BaseModel


class OwnerCreateRequest(BaseModel):
    name: str
    document: str
    date_of_birth: date
