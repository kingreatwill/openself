import models


class Domain:
    def __init__(self, model: models.db.Document):
        self.model = model

    # 列表;
    def list(self, size=10, index=1, **kwargs):
        size = int(size)
        index = int(index)
        return self.model.objects(**kwargs).skip((index - 1) * size).limit(size)

    # 明细;
    def get(self, id):
        return self.model.objects(**{self.model.key(): id}).first()

    def update(self, id, **kwargs):
        model = self.model.objects(**{self.model.key(): id}).first()
        if model:
            return model.update(**kwargs)
        return True
