# 上传文件
import dataclasses
import os

from bson import ObjectId
from gridfs import GridFS
from mongoengine import get_db
import typing

from core import filelib


@dataclasses.dataclass
class FileMeta:
    file_id: ObjectId
    mimetype: str
    sha1: str
    md5: str
    length: int
    extension: str


def __put(f, name):
    fs = GridFS(get_db())
    # 计算文件属性
    extension = os.path.splitext(name)[1]
    mimetype = filelib.mime(f)
    sha1 = filelib.sha1(f)
    md5 = filelib.md5(f)
    arg = {'mimetype': mimetype, 'sha1': sha1, 'md5': md5}
    exist_fs = fs.find_one(arg)
    if exist_fs:
        return FileMeta(file_id=exist_fs._id, length=exist_fs.length, extension=newfile.extension, **arg)

    newfile = fs.new_file(content_type=mimetype, name=name, extension=extension, **arg)
    newfile.write(f)
    newfile.close()
    return FileMeta(file_id=newfile._id, length=newfile.length, extension=newfile.extension, **arg)


def put(file, name=None):
    if isinstance(file, str):
        with open(file, 'rb') as fd:
            if not name:
                name = os.path.basename(file)
            return __put(fd, name)
    return __put(file, name)


# 获取文件
def get(id):
    if isinstance(id, str):
        id = ObjectId(id)
    return GridFS(get_db()).get(id)
