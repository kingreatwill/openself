import datetime
import decimal
import uuid
from bson import json_util, ObjectId
from flask.json import JSONEncoder
from mongoengine import QuerySet
from mongoengine.base import BaseDocument


class RecallJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, dict):
            return o
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            """
            model 定义了 keys 方法 和__getitem__方法的可以直接转换成字典
            """
            return dict(o)
        if isinstance(o, datetime.datetime):
            # 格式化时间
            return o.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(o, datetime.date):
            # 格式化日期
            return o.strftime('%Y-%m-%d')
        if isinstance(o, decimal.Decimal):
            # 格式化高精度数字
            return str(o)
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, uuid.UUID):
            # 格式化uuid
            return str(o)
        if isinstance(o, bytes):
            # 格式化字节数据
            return o.decode("utf-8")
        if isinstance(o, BaseDocument):
            return json_util._json_convert(o.to_mongo())
            # data = o.to_mongo()
            # o_id = data.pop('_id', None)
            # if o_id:
            #     data['id'] = str(o_id['$oid'])
            # data.pop('_cls', None)
            # return data

        if isinstance(o, QuerySet):
            # json_util._json_convert(o.as_pymongo())
            return [RecallJSONEncoder.default(self, rc) for rc in o]

        return JSONEncoder.default(self, o)
