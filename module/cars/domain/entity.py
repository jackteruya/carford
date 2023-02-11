from pydantic import BaseModel

from module.owners.domain.entity import Owner


class Car(BaseModel):
    id: int
    name: str
    color: str
    model: str
    owner: Owner
