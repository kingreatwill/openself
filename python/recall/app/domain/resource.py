from core import mongolib
from domain import Domain
from models import Resource


class ResourceDomain(Domain):
    def __init__(self):
        super().__init__(Resource)

    def list(self):
        return self.model.objects[0:10]

    def create(self, **kwargs):
        model = self.model()
        model.blob_id = mongolib.put()
        for name, value in kwargs.items():
            setattr(model, name, value)
        return self.model.save()
