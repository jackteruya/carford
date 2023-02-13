from marshmallow import Schema, fields


class OwnerCreateRequest(Schema):
    name = fields.String(required=True)
    document = fields.String(required=True)
    date_of_birth = fields.Date(required=True)
