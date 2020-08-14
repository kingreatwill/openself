import unittest

from core import filelib


class TestCore(unittest.TestCase):
    def test_filelib(self):
        print(filelib.mime('xxx.jpg'))


if __name__ == '__main__':
    unittest.main()
