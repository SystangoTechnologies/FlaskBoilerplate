from __future__ import print_function
from __future__ import unicode_literals

import os
from pymongo import MongoClient


# connect MongoDB
def configure_mongo():
    client = MongoClient(os.environ.get('DB_URL'))
    client.db = client[os.environ.get('DB_NAME')]
    return client
