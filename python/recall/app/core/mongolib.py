# 上传文件
import dataclasses

from bson import ObjectId
from gridfs import GridFS
from mongoengine import get_db
from werkzeug.datastructures import FileStorage

from core import filelib


@dataclasses.dataclass
class FileMeta:
    file_id: ObjectId
    mimetype: str
    sha1: str
    md5: str


def __put(f):
    fs = GridFS(get_db())
    # 计算文件属性
    mimetype = filelib.mime(f)
    sha1 = filelib.sha1(f)
    md5 = filelib.md5(f)
    arg = {'mimetype': mimetype, 'sha1': sha1, 'md5': md5}
    exist_fs = fs.find_one(arg)
    if exist_fs:
        return FileMeta(file_id=exist_fs._id,
                        **{'mimetype': exist_fs.mimetype, 'sha1': exist_fs.sha1, 'md5': exist_fs.md5})

    return FileMeta(file_id=fs.put(f, content_type=mimetype, **arg),
                    **arg)


def put(file):
    if isinstance(file, str):
        with open(file, 'rb') as fd:
            return __put(fd)
    return __put(file)


# 获取文件
def get(id):
    if isinstance(id, str):
        id = ObjectId(id)
    return GridFS(get_db()).get(id)
