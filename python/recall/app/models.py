from datetime import datetime
from bson import ObjectId
from flask_mongoengine import MongoEngine

db = MongoEngine()


class ResourceBlob(db.Document):
    blob_id = db.ObjectIdField(default=ObjectId(), required=True, primary_key=True)
    hash = db.StringField(required=True, max_length=50)
    md5 = db.StringField(required=True, max_length=50)
    blob = db.FileField(required=True, db_alias='recall-db-alias')
    create_time = db.DateTimeField(default=datetime.now(), required=True)

    meta = {'db_alias': 'recall-db-alias'}

    def keys(self):
        return ["blob_id", "hash", "md5", "blob", "create_time"]

    def __getitem__(self, item):
        return getattr(self, item)


class Resource(db.Document):
    resource_id = db.ObjectIdField(default=ObjectId(), required=True, primary_key=True)
    blob_id = db.ObjectIdField(required=True)
    title = db.StringField(max_length=50)
    tags = db.ListField(db.StringField(max_length=30, required=True))
    create_time = db.DateTimeField(default=datetime.now(), required=True)

    meta = {'db_alias': 'recall-db-alias'}

    def keys(self):
        return ["resource_id", "blob_id", "title", "tags", "create_time"]

    def __getitem__(self, item):
        return getattr(self, item)
