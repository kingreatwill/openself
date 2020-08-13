from datetime import datetime
from bson import ObjectId
from mongoengine import *


class ResourceBlob(Document):
    blob_id = ObjectIdField(default=ObjectId(), required=True, primary_key=True)
    hash = StringField(required=True, max_length=50)
    md5 = StringField(required=True, max_length=50)
    blob = FileField(required=True, db_alias='recall-db-alias')
    create_time = DateTimeField(default=datetime.now(), required=True)

    meta = {'db_alias': 'recall-db-alias'}


class Resource(Document):
    resource_id = ObjectIdField(default=ObjectId(), required=True, primary_key=True)
    blob_id = ObjectIdField(required=True)
    title = StringField(max_length=50)
    tags = ListField(StringField(max_length=30, required=True))
    create_time = DateTimeField(default=datetime.now(), required=True)

    meta = {'db_alias': 'recall-db-alias'}
