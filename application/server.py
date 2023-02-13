from flask import Blueprint, Flask
from flask_cors import CORS
from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from application.rest.owners.owner_create import api_owner_create
from application.rest.owners.owner_get import owner_get_namespace


class ServeApplication:

    def __init__(self):
        self.app = Flask(__name__)
        self._blueprint = Blueprint("api", __name__, url_prefix="/api/v1")

    def _init_blueprints(self, app):
        api = Api(
            self._blueprint,
            title="CarFord",
            version="0.0.1",
            doc="/docs",
        )

        api.add_namespace(owner_get_namespace)
        api.add_namespace(api_owner_create)
        app.register_blueprint(self._blueprint)

    def create_app(self):
        # self.app.wsgi_app = ProxyFix(self.app.wsgi_app)

        self._init_blueprints(self.app)
        CORS(self.app)

        return self.app


app = ServeApplication().create_app()
