from flask_restx import Model
from marshmallow import Schema, fields


class OwnerCreateRequest(Schema):
    name = fields.String(required=True)
    document = fields.String(required=True)
    date_of_birth = fields.Date(required=True)


resource_fields = Model('Owner', {
    'name': fields.String,
    'document': fields.String,
    'date_of_birth': fields.Date,
})

response_fields = Model('Owner Response', {
    'id': fields.Integer,
    'name': fields.String,
    'document': fields.String,
    'date_of_birth': fields.Date,
})
