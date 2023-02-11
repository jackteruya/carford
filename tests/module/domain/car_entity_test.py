from datetime import date

import pytest
from pytest import fixture

from module.cars.domain.entity import Car
from module.owners.domain.entity import Owner
from utils.constants import ColorCar, ModelCar


@fixture
def car_data():
    return {
        "id": 1,
        "name": "Pytest",
        "color": ColorCar.BLUE.value,
        "model": ModelCar.HATCH.value,
        "owner": Owner(
            id=1,
            name="Pytest",
            document="55555555555",
            date_of_birth=date(year=1990, month=2, day=9)
        )
    }


def test_entity_car(car_data):
    data = car_data
    car_entity = Car(**data)

    assert car_entity.id == data.get("id")
    assert car_entity.name == data.get("name")
    assert car_entity.color == data.get("color")
    assert car_entity.model == data.get("model")
    assert car_entity.owner == data.get("owner")


def test_entitfy_car_color_no_register(car_data):
    data = car_data
    data['color'] = 'Black'
    with pytest.raises(ValueError):
        Car(**data)


def test_entitfy_car_model_no_register(car_data):
    data = car_data
    data['model'] = 'SUV'
    with pytest.raises(ValueError):
        Car(**data)

