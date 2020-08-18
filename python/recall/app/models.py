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
    mimetype = StringField(max_length=200)
    sha1 = StringField(max_length=100)
    md5 = StringField(max_length=100)
    length = LongField()
    extension = StringField(max_length=20)
    create_time = DateTimeField(default=datetime.now(), required=True)

    @staticmethod
    def key():
        return "resource_id"

    def keys(self):
        return ["resource_id", "blob_id", "filename", "title", "tags", "mimetype", "sha1", "md5", "length",
                "extension","create_time"]

    def __getitem__(self, item):
        return getattr(self, item)
