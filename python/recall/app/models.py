from datetime import datetime
from bson import ObjectId
from flask_mongoengine import MongoEngine
from mongoengine import *

db = MongoEngine()


class Resource(db.Document):
    resource_id = ObjectIdField(default=ObjectId(), required=True, primary_key=True)
    blob_id = ObjectIdField(required=True)
    filename = StringField(max_length=100)
    title = StringField(max_length=50)
    tags = ListField(StringField(max_length=30, required=True))
    create_time = DateTimeField(default=datetime.now(), required=True)

    @staticmethod
    def key():
        return "resource_id"

    def keys(self):
        return ["resource_id", "blob_id", "filename", "title", "tags", "create_time"]

    def __getitem__(self, item):
        return getattr(self, item)
