from module.owners.domain.use_case import OwnerUseCase
from module.owners.dto.owner_request import OwnerCreateRequest
from repository.owner_repository import OwnerRepository


class OwnerController:
    
    @staticmethod
    def get_owner_by_id(id):
        return OwnerUseCase(OwnerRepository()).get_owner_by_id(id)
    
    @staticmethod
    def create_owner(data: dict):
        data = OwnerCreateRequest(**data)
        return OwnerUseCase(OwnerRepository()).create_owner(data)
