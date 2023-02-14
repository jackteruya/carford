import json

from flask import Response
from flask_restx import Namespace, Resource, fields
from flask_restx._http import HTTPStatus

from application.rest.cars.schema.car import CarCreateRequest
from application.rest.status import STATUS_CODES
from module.cars.controller.car_controller import CarController
from module.cars.serializers.car import CarJsonEncoder
from utils.constants import ColorCar, ModelCar

api_car_create = Namespace("car", description="Endpoints to post car")


resource_fields = api_car_create.model('Car', {
    'name': fields.String(required=True),
    'color': fields.String(required=True, choices=ColorCar.options_values()),
    'model': fields.String(required=True, choices=ModelCar.options_values()),
    'owner_id': fields.Integer(required=True)
})

response_fields = api_car_create.model('Car Response', {
    'id': fields.Integer,
    'name': fields.String,
    'color': fields.String,
    'model': fields.String,
    'owner_id': fields.Integer,
})


@api_car_create.route('/', methods=['POST'])
class OwnerGetResource(Resource):
    """Create Car"""

    @api_car_create.expect(resource_fields)
    @api_car_create.response(HTTPStatus.CREATED.value, description='', model=response_fields)
    def post(self):
        try:
            data = CarCreateRequest().load(api_car_create.payload)
            response = CarController().create_car(data)
            return Response(
                json.dumps(response.value, cls=CarJsonEncoder),
                mimetype="application/json",
                status=STATUS_CODES[response.type],
            )

        except ValueError as exc:
            return Response(
                json.dumps({'msg': exc.args[0]}),
                mimetype="application/json",
                status=HTTPStatus.BAD_REQUEST.value
            )

        except Exception as exc:
            return Response(
                json.dumps({"msg": 'Bad request'}),
                mimetype="application/json",
                status=HTTPStatus.BAD_REQUEST.value
            )
