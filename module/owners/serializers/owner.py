import json


class OwnerJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            to_serialize = {
                "id": obj.id,
                "name": obj.name,
                "document": obj.document,
                "date_of_birth": str(obj.date_of_birth),
            }
            return to_serialize
        except AttributeError:  # pragma: no cover
            return super().default(obj)
