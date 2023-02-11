from datetime import date

from pytest import fixture

from module.cars.domain.entity import Car
from module.owners.domain.entity import Owner
from tests.module.domain.owner_entity_test import owner_entity_data


@fixture
def car_data():
    return {
        "id": 1,
        "name": "Pytest",
        "color": "55555555555",
        "model": "blue",
        "owner": Owner(
            id=1,
            name="Pytest",
            document="55555555555",
            date_of_birth=date(year=1990, month=2, day=9)
        )
    }


def test_entity_owner(car_data):
    data = car_data
    car_entity = Car(**data)

    assert car_entity.id == data.get("id")
    assert car_entity.name == data.get("name")
    assert car_entity.color == data.get("color")
    assert car_entity.model == data.get("model")
    assert car_entity.owner == data.get("owner")
