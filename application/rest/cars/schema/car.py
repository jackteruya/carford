from flask_restx import Model
from marshmallow import Schema, fields


class CarCreateRequest(Schema):
    name = fields.String(required=True)
    color = fields.String(required=True)
    model = fields.String(required=True)
    owner_id = fields.Integer(required=True)
