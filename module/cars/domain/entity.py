from pydantic import BaseModel, validator

from module.owners.domain.entity import Owner
from utils.constants import ColorCar, ModelCar


class Car(BaseModel):
    id: int
    name: str
    color: str
    model: str
    owner: Owner

    @validator('color')
    def color_car(cls, value):
        if value not in ColorCar.options_values():
            raise ValueError("color not registered")
        return value

    @validator('model')
    def model_car(cls, value):
        if value not in ModelCar.options_values():
            raise ValueError("model not registered")
        return value
