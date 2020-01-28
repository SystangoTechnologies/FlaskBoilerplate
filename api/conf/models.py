from __future__ import print_function
from __future__ import unicode_literals
import importlib

from api.utils.mongodb import MongoDBModel
from api.utils.basic import get_class_objs


def load_models(tools):
    '''function to load models'''
    db_models = {}
    mongo = tools['mongo']
    mod = importlib.import_module('api.model')

    models = get_class_objs(mod, MongoDBModel)

    for model in models:
        name = model.coll_name
        collection = mongo.db[name]
        db_models[name] = model(collection)

    return db_models
