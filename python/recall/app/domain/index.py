from domain import Domain
from models import *


class IndexDomain(Domain):
    def list(self):
        return Resource.objects[0:10]

    def img(self, id):
        r = Resource.objects(resource_id=id).first()
        if r:
            b = ResourceBlob.objects(blob_id=r.blob_id).first()
            if b:
                return b, r
        return None, None

    def detail(self, id):
        return Resource.objects(resource_id=id).first()
