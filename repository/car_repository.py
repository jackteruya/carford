from sqlalchemy.exc import NoResultFound

from infra.db import DBConnectionHandler
from module.cars.domain.entity import Car
from module.cars.interface.car_repo_interface import CarRepositoryInterface
from module.owners.domain.entity import Owner
from repository.models import Cars


class CarRepository(CarRepositoryInterface):
    """Car Repository"""

    def __init__(self):
        self._db_connection = DBConnectionHandler

    def _car(self, data):
        return Car(
            id=data.id,
            name=data.name,
            color=data.color,
            model=data.model,
            owner=Owner(
                id=data.owner.id,
                name=data.owner.name,
                document=data.owner.document,
                date_of_birth=data.owner.date_of_birth,
            ),
        )

    def get_by_id(self, id: int):
        try:
            with self._db_connection() as db_connection:
                data = (
                    db_connection.session.query(Cars)
                    .filter_by(id=id)
                    .first()
                )
                return self._car(data)

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
        finally:
            db_connection.session.close()

    def get_by_owner_id(self, owner_id: int):
        try:
            with self._db_connection() as db_connection:
                list_data = (
                    db_connection.session.query(Cars)
                    .filter_by(owner_id=owner_id)
                    .all()
                )
                return [self._car(data) for data in list_data]

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
        finally:
            db_connection.session.close()

    def create_car(self, name: str, color: str, model: str, owner_id: int):
        try:
            with self._db_connection() as db_connection:
                new_car = Cars(name=name, color=color, model=model, owner_id=owner_id)
                db_connection.session.add(new_car)
                db_connection.session.commit()
                db_connection.session.refresh(new_car)
                return self._car(new_car)

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
