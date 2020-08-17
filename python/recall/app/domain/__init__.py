from mongoengine import connect

from models import *


class Domain:
    def __init__(self, model):
        self.model = model

    def get(self, id):
        return self.model.objects(**{self.model.key(): id}).first()
