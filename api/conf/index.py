from __future__ import print_function
from __future__ import unicode_literals

import os

from flask_cors import CORS

from .auth import configure_auth
from .mongo import configure_mongo
from .models import load_models
from api.utils.mission import *


# configure query app
def configure_app(app):
    '''function to configure app'''
    CORS(app) # cross domain

    tools = {
        'auth': configure_auth(),
        'mongo': configure_mongo()
    }

    models = load_models(tools)

    if os.environ.get('REFRESH_DATA', False):
        init_tasks(models)

    return tools
