from __future__ import print_function
from __future__ import unicode_literals

from datetime import datetime

from bson import ObjectId

from api.utils.basic import Model


class MongoDBModel(Model):
    coll_name = None
    fields = None

    def __init__(self, collection):
        self.collection = collection
        self.on_init()

    def on_init(self):
        pass

    @staticmethod
    def __transform_doc(doc):
        doc['_id'] = str(doc['_id'])
        return doc

    def get_valid_obj(self, obj):
        # check fields
        valid_obj = {}
        if not self.fields:
            valid_obj = obj.copy()
        else:
            for f in self.fields:
                valid_obj[f] = obj[f]
        return valid_obj

    def find(self):
        docs = map(self.__transform_doc, self.collection.find())
        return docs

    def find_by_id(self, id):
        doc = self.collection.find_one({'_id': ObjectId(id)})
        return None if doc is None else self.__transform_doc(doc)

    def create(self, obj):
        obj['created_at'] = datetime.now()
        obj['updated_at'] = datetime.now()
        valid_obj = self.get_valid_obj(obj)
        result = self.collection.insert_one(valid_obj)
        valid_obj['_id'] = str(result.inserted_id)
        return valid_obj

    def update_by_id(self, id, obj):
        doc = self.find_by_id(id)
        if doc is None:
            return None

        obj['created_at'] = doc['created_at']
        obj['updated_at'] = datetime.now()
        valid_obj = self.get_valid_obj(obj)
        self.collection.update_one(
            {'_id': ObjectId(id)},
            {'$set': valid_obj})

        doc.update(valid_obj)
        return self.__transform_doc(doc)

    def remove_by_id(self, id):
        doc = self.find_by_id(id)
        if doc is None:
            return False
        else:
            self.collection.remove({'_id': ObjectId(id)})
            return True
