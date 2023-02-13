import json

from flask import Response
from flask_restx import Namespace, Resource

from application.rest.status import STATUS_CODES
from module.owners.controller.owner_controller import OwnerController
from module.owners.serializers.owner import OwnerJsonEncoder

owner_get_namespace = Namespace("owner", description="Endpoints to get tickets")


@owner_get_namespace.route('/<int:id>', methods=['GET'])
class OwnerGetReource(Resource):
    """Get Owner by id"""

    def get(self, id):
        response = OwnerController().get_owner_by_id(id)
        return Response(
            json.dumps(response.value, cls=OwnerJsonEncoder),
            mimetype="application/json",
            status=STATUS_CODES[response.type],
        )
