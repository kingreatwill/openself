import unittest

from bson import ObjectId
from mongoengine import connect

from core import filelib, mongolib


class TestCore(unittest.TestCase):
    def test_filelib(self):
        print(filelib.mime('xxx.jpg'))

    def test_mongolib(self):
        connect(db='recall',host='127.0.0.1', port=27017)
        print(mongolib.put('xxx.jpg'))
        print(mongolib.get('5f3a1ed448ee3f12057317e1'))
        print(mongolib.get(ObjectId('5f3a1ed448ee3f12057317e1')))


if __name__ == '__main__':
    unittest.main()
