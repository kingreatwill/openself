from PIL import Image

def to_model(dic):
    Model = type('Model', (object,), dic)
    return Model()



