import json


class CarJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            to_serialize = {
                "id": obj.id,
                "name": obj.name,
                "color": obj.color,
                "model": obj.model,
                "owner": {
                    "id": obj.owner.id,
                    "name": obj.owner.name,
                    "date_of_birth": str(obj.owner.date_of_birth),
                },
            }
            return to_serialize
        except AttributeError:  # pragma: no cover
            return super().default(obj)
