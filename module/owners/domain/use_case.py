from module.owners.dto.owner_request import OwnerCreateRequest
from module.owners.interface.owner_repo_interface import OwnerRepositoryInterface


class OwnerUseCase:

    def __init__(self, repository: OwnerRepositoryInterface) -> None:
        self._repository = repository

    def create_owner(self, data: OwnerCreateRequest):
        return self._repository.create_owner(
            name=data.name, document=data.document, date_of_birth=data.date_of_birth
        )

    def get_owner_by_id(self, id: int):
        return self._repository.get_by_id(id)

