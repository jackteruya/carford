from datetime import date

from pytest import fixture

from module.owners.domain.entity import Owner


@fixture
def owner_entity_data():
    return {
        "id": 1,
        "name": "Pytest",
        "document": "55555555555",
        "date_of_birth": date(year=1990, month=2, day=9)
    }


def test_entity_owner(owner_entity_data):
    data = owner_entity_data
    owner_entity = Owner(**owner_entity_data)

    assert owner_entity.id == data.get("id")
    assert owner_entity.name == data.get("name")
    assert owner_entity.document == data.get("document")
    assert owner_entity.date_of_birth == data.get("date_of_birth")
