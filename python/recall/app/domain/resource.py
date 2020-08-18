import os

from core import mongolib
from domain import Domain
from models import Resource


class ResourceDomain(Domain):
    def __init__(self):
        super().__init__(Resource)

    def create(self, files: dict, **kwargs):
        create_models = []
        for (name, f) in files.items():
            meta = mongolib.put(f, name)
            model = self.model()
            model.blob_id = meta.file_id
            model.filename = name
            model.title = kwargs["title"]
            model.tags = kwargs["tags"].split(',')
            model.mimetype = meta.mimetype
            model.sha1 = meta.sha1
            model.md5 = meta.md5
            model.length = meta.length
            model.extension = os.path.splitext(name)[1].lower()
            model.save()
            create_models.append(model)
        return create_models

