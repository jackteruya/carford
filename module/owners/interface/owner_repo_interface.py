from abc import ABC, abstractmethod
from datetime import date


class OwnerRepositoryInterface(ABC):
    """Interface to Owner Repository"""

    @abstractmethod
    def get_by_id(self, id: int):
        """abstractmethod"""

        raise Exception("Method not implemented")

    @abstractmethod
    def create_owner(self, name: str, document: str, date_of_birth: date):
        """abstractmethod"""

        raise Exception("Method not implemented")
