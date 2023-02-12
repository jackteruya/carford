from sqlalchemy.exc import NoResultFound

from infra.db import DBConnectionHandler
from module.cars.interface.car_repo_interface import CarRepositoryInterface
from repository.models import Cars


class CarRepository(CarRepositoryInterface):
    """Car Repository"""

    def __init__(self):
        self._db_connection = DBConnectionHandler

    def get_by_id(self, id: int):
        try:
            with self._db_connection() as db_connection:
                data = (
                    db_connection.session.query(Cars)
                    .filter_by(id=id)
                    .first()
                )
                return data

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
        finally:
            db_connection.session.close()

    def get_by_owner_id(self, owner_id: int):
        try:
            with self._db_connection() as db_connection:
                data = (
                    db_connection.session.query(Cars)
                    .filter_by(owner_id=owner_id)
                    .all()
                )
                return data

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
                return new_car

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
