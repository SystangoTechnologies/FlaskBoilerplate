'''
    Module to import all APIs
'''

from flask_cors import CORS
from flask_restplus import Api
from flask import Blueprint, url_for

from .task import NS as task_ns


api_blueprint = Blueprint("api_v1", __name__, url_prefix="/api/v1")
CORS(api_blueprint)

class CustomApi(Api):
    @property
    def specs_url(self):
        scheme = 'http' if '5000' in self.base_url else 'https'
        return url_for(self.endpoint('specs'), _external=True, _scheme=scheme)

API = CustomApi(
    api_blueprint,
    title="Task APIs",
    version="1.0"
)

API.add_namespace(task_ns)
