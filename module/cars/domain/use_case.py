from module.cars.dto.car_request import CarCreateRequest
from module.cars.interface.car_repo_interface import CarRepositoryInterface
from module.response import ResponseFailure, ResponseSuccess, ResponseTypes
from utils.constants import ColorCar, ModelCar


class CarUseCase:

    def __init__(self, repository: CarRepositoryInterface) -> None:
        self._repository = repository

    def create_car(self, data: CarCreateRequest):
        self.validate_regiter_car(data)

        car = self._repository.create_car(
            name=data.name,
            color=data.color.lower(),
            model=data.model.lower(),
            owner_id=data.owner_id
        )
        if not car:
            return ResponseFailure(ResponseTypes.PARAMETERS_ERROR, 'Not Found')
        return ResponseSuccess(car)

    def get_car_by_id(self, id: int):
        car = self._repository.get_by_id(id)
        if not car:
            return ResponseFailure(ResponseTypes.PARAMETERS_ERROR, 'Not Found')
        return ResponseSuccess(car)

    def get_car_by_owner_id(self, owner_id):
        car = self._repository.get_by_owner_id(owner_id)
        if not car:
            return ResponseFailure(ResponseTypes.PARAMETERS_ERROR, 'Not Found')
        return ResponseSuccess(car)

    def get_amount_of_car_by_owner(self, owner_id):
        return len(self.get_car_by_owner_id(owner_id).value)

    def validate_regiter_car(self, data):
        if self.get_amount_of_car_by_owner(data.owner_id) >= 3:
            raise ValueError("owner has 3 or more cars")
        if self.validate_color(data.color):
            raise ValueError("invalid color")
        if self.validate_model(data.model):
            raise ValueError("invalid model")

    def validate_color(self, color):
        if color.lower() not in ColorCar.options_values():
            return True
        return False

    def validate_model(self, model):
        if model.lower() not in ModelCar.options_values():
            return True
        return False
