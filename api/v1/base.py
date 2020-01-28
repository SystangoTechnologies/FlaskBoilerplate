'''
    Module to load models
'''
from __future__ import print_function
from __future__ import unicode_literals

from api.conf.models import load_models
from api.conf.auth import configure_auth
from api.conf.mongo import configure_mongo


def get_models():
    '''function get all models'''
    tools = {
        'auth': configure_auth(),
        'mongo': configure_mongo()
    }

    models = load_models(tools)
    return models

models = get_models()
