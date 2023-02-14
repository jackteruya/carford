from module.cars.domain.use_case import CarUseCase
from module.cars.dto.car_request import CarCreateRequest
from repository.car_repository import CarRepository


class CarController:
    
    @staticmethod
    def get_car_by_id(id):
        return CarUseCase(CarRepository()).get_car_by_id(id)

    @staticmethod
    def get_car_by_owner_id(id):
        return CarUseCase(CarRepository()).get_car_by_owner_id(id)
    
    @staticmethod
    def create_car(data: dict):
        data = CarCreateRequest(**data)
        return CarUseCase(CarRepository()).create_car(data)
