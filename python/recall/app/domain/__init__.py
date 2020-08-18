from mongoengine import connect

from models import *


class Domain:
    def __init__(self, model):
        self.model = model
    # 列表;
    def list(self, **kwargs):
        return self.model.objects[0:10]
    # 明细;
    def get(self, id):
        return self.model.objects(**{self.model.key(): id}).first()
