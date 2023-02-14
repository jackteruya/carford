import json

from flask import Response
from flask_restx import Namespace, Resource, fields
from flask_restx._http import HTTPStatus
from pydantic import ValidationError

from application.rest.owners.schema.owner import OwnerCreateRequest
from application.rest.status import STATUS_CODES
from module.owners.controller.owner_controller import OwnerController
from module.owners.serializers.owner import OwnerJsonEncoder

api_owner_create = Namespace("owner", description="Endpoints to get tickets")


resource_fields = api_owner_create.model('Owner', {
    'name': fields.String,
    'document': fields.String,
    'date_of_birth': fields.Date,
})

response_fields = api_owner_create.model('Owner response', {
    'id': fields.Integer,
    'name': fields.String,
    'document': fields.String,
    'date_of_birth': fields.Date,
})


@api_owner_create.route('/', methods=['POST'])
class OwnerCreateResource(Resource):
    """Create Owner"""

    @api_owner_create.expect(resource_fields)
    @api_owner_create.response(HTTPStatus.OK.value, description='', model=response_fields)
    def post(self):
        try:
            data = OwnerCreateRequest().load(api_owner_create.payload)
            response = OwnerController().create_owner(data)
            return Response(
                json.dumps(response.value, cls=OwnerJsonEncoder),
                mimetype="application/json",
                status=STATUS_CODES[response.type],
            )

        except ValidationError as exc:
            return Response(
                json.dumps(exc.args[0]),
                mimetype="application/json",
                status=HTTPStatus.BAD_REQUEST.value
            )

        except Exception as exc:
            print(exc)
            return Response(
                json.dumps(exc.args[0]),
                mimetype="application/json",
                status=HTTPStatus.BAD_REQUEST.value
            )
