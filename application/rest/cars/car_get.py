import json

from flask import Response
from flask_restx import Namespace, Resource

from application.rest.status import STATUS_CODES
from module.cars.controller.car_controller import CarController
from module.cars.serializers.car import CarJsonEncoder

api_car_get = Namespace("car", description="Endpoints to get car")


@api_car_get.route('/<int:id>', methods=['GET'])
class OwnerGetReource(Resource):
    """Get Owner by id"""

    def get(self, id):
        response = CarController().get_car_by_id(id)
        return Response(
            json.dumps(response.value, cls=CarJsonEncoder),
            mimetype="application/json",
            status=STATUS_CODES[response.type],
        )


@api_car_get.route('/owner/<int:owner_id>', methods=['GET'])
class OwnerGetReource(Resource):
    """Get Owner by id"""

    def get(self, owner_id):
        response = CarController().get_car_by_owner_id(owner_id)
        return Response(
            json.dumps(response.value, cls=CarJsonEncoder),
            mimetype="application/json",
            status=STATUS_CODES[response.type],
        )
