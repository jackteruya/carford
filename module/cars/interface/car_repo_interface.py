from abc import ABC, abstractmethod


class CarRepositoryInterface(ABC):
    """Interface to Car Repository"""

    @abstractmethod
    def get_by_id(self, id: int):
        """abstractmethod"""

        raise Exception("Method not implemented")

    @abstractmethod
    def get_by_owner_id(self, owner_id: int):
        """abstractmethod"""

        raise Exception("Method not implemented")

    @abstractmethod
    def create_car(self, name: str, color: str, model: str, owner_id: int):
        """abstractmethod"""

        raise Exception("Method not implemented")
