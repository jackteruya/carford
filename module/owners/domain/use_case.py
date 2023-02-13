from module.owners.dto.owner_request import OwnerCreateRequest
from module.owners.interface.owner_repo_interface import OwnerRepositoryInterface
from module.response import ResponseSuccess, ResponseFailure, ResponseTypes


class OwnerUseCase:

    def __init__(self, repository: OwnerRepositoryInterface) -> None:
        self._repository = repository

    def create_owner(self, data: OwnerCreateRequest):
        owner = self._repository.create_owner(
            name=data.name, document=data.document, date_of_birth=data.date_of_birth
        )
        if not owner:
            return ResponseFailure(ResponseTypes.PARAMETERS_ERROR, 'Not Found')
        return ResponseSuccess(owner)

    def get_owner_by_id(self, id: int):
        owner = self._repository.get_by_id(id)
        if not owner:
            return ResponseFailure(ResponseTypes.PARAMETERS_ERROR, 'Not Found')
        return ResponseSuccess(owner)
