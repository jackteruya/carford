from datetime import date

from sqlalchemy.exc import NoResultFound

from infra.db import DBConnectionHandler
from module.owners.domain.entity import Owner as OwnerDomain
from module.owners.interface.owner_repo_interface import OwnerRepositoryInterface
from repository.models import Owners


class OwnerRepository(OwnerRepositoryInterface):
    """Owner Repository"""

    def __init__(self):
        self._db_connection = DBConnectionHandler

    def _owner(self, data):
        return OwnerDomain(
            id=data.id,
            name=data.name,
            document=data.document,
            date_of_birth=data.date_of_birth,
        )

    def get_by_id(self, id: int):
        try:
            with self._db_connection() as db_connection:
                data = (
                    db_connection.session.query(Owners)
                    .filter_by(id=id)
                    .first()
                )
                return self._owner(data)

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
        finally:
            db_connection.session.close()

    def create_owner(self, name: str, document: str, date_of_birth: date):
        try:
            with self._db_connection() as db_connection:
                new_owner = Owners(name=name, document=document, date_of_birth=date_of_birth)
                db_connection.session.add(new_owner)
                db_connection.session.commit()
                db_connection.session.refresh(new_owner)
                return self._owner(new_owner)

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
