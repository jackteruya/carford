import json

from flask import Response
from flask_restx import Namespace, Resource
from flask_restx._http import HTTPStatus

from application.rest.owners.schema.owner import response_fields
from application.rest.status import STATUS_CODES
from module.owners.controller.owner_controller import OwnerController
from module.owners.serializers.owner import OwnerJsonEncoder

api_owner_get = Namespace("owner", description="Endpoints to get tickets")


@api_owner_get.route('/<int:id>', methods=['GET'])
class OwnerGetReource(Resource):
    """Get Owner by id"""

    @api_owner_get.response(HTTPStatus.OK.value, description='', model=response_fields)
    def get(self, id):
        response = OwnerController().get_owner_by_id(id)
        return Response(
            json.dumps(response.value, cls=OwnerJsonEncoder),
            mimetype="application/json",
            status=STATUS_CODES[response.type],
        )
