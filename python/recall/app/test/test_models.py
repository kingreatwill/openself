import unittest

from bson import ObjectId
from gridfs import GridFS
from mongoengine import connect, get_db
from werkzeug.datastructures import FileStorage

from core import filelib
from test import models


class TestModels(unittest.TestCase):
    def setUp(self):
        connect(db='recall', alias="recall-db-alias", host='127.0.0.1', port=27017)
        # 如需验证和指定主机名 http://docs.mongoengine.org/guide/connecting.html#connecting-to-mongodb
        # connect('blog', host='127.0.0.1', port=27017, username='root', password='1234')
        # http://docs.mongoengine.org/guide/gridfs.html#writing

    def test_model(self):
        blob = models.ResourceInfo()
        print(dict(blob))

    def test_save(self):
        # create a user
        # u = User.create_user(username='name', password='admin', email='mail@ex.com')
        blob = models.ResourceBlob()
        blob_id = blob.blob_id
        with open('xxx.jpg', 'rb') as fd:
            # 计算文件属性;
            content_type = filelib.mime(fd)
            blob.hash = filelib.sha1(fd)
            blob.md5 = filelib.md5(fd)
            # 检查文件是否存在;
            exist_blob = models.ResourceBlob.objects(md5=blob.md5).first()
            if not exist_blob:
                # 保存文件；
                blob.blob.put(fd, content_type=content_type, hash="xxxx")
                blob.blob.write()
                blob.save()
            blob_id = exist_blob.blob_id
        # 文件元信息保存;
        basic = models.ResourceInfo(blob_id=blob_id, title="filename", tags=["ai", "bigdata"])
        basic.save()

    def test_save2(self):
        blob = models.ResourceBlob()
        blob.hash = "xx"
        blob.md5 = "xx"
        blob.blob.grid_id = ObjectId("5f34ff38951582d0847ee108")
        blob.blob._mark_as_changed()
        blob.save()

    def test_save3(self):
        # 测试删除是否会删除文件；答案：会！设计时要注意！！！
        models.ResourceBlob.objects.get(blob_id='5f35f477ef9902520ea63a1a').delete()

    def test_fs(self):
        fs = GridFS(get_db(alias="recall-db-alias"))
        # with open('xxx.jpg', 'rb') as fd:
        #     id = fs.put(fd)
        #     print(id)
        b = fs.get(ObjectId("5f39fd75e9974144d72231eb"))
        b2 = fs.find_one({"md5": "c3c1ae262ddd527f0465dfb77a546b73"})

        print(1)

    def test_update(self):
        # 返回所有符合查询条件的结果的文档对象列表
        rs = models.ResourceInfo.objects(title="filename").first()
        # 更新查询到的文档:http://docs.mongoengine.org/guide/querying.html?highlight=update#atomic-updates
        rs.update(push__tags="tag_end")  # 追加，不能是数组
        # rs.update(push__tags__0=["tag"]) # 指定位置追加，可以多个
        # models.Resource.objects(tags='tag_end').update(set__tags__S='mongodb') # 更新tag_end = mongodb，只更新第一个位置的
        rs.update(tags=["fin_tag"])
        # rs.update(set__tags=["fin_tag","xx"]) # 同上

    def test_select(self):
        # # 返回集合里的所有文档对象的列表
        f = models.ResourceBlob.objects.all().first()
        b = f.blob.get()
        all_blob = models.ResourceBlob.objects.all()
        print(all_blob.to_json())
        print(all_blob.as_pymongo())
        # Order by ascending date first, then descending title
        # blogs = BlogPost.objects().order_by('+date', '-title')
        # 5 users, starting from the 11th user found
        # users = User.objects[10:15]  # limit() and skip()
        # comments - skip 5, limit 10
        # Page.objects.fields(slice__comments=[5, 10])
        # # 这里默认导入了之前的类型
        # image_first = models.ResourceBlob.objects(desription="this is a demo image").first()
        # image = image_first.blob.read()
        # content_type = image.image

        # 将会返回所有tags包含coding的文档
        # Posts.objects(tags='coding')


# def report(request):
#     if request.method == 'POST':
#
#         report_form = ResourceBlob(title=request.POST.get('title'))
#
#         f = request.FILES['report']
#
#         # 这里打印的是文件名
#         print(f)
#
#         # 通过流保存文件
#         report_form.blob.new_file()
#
#         for chunk in f.chunks():
#             report_form.blob.write(chunk)
#
#         report_form.blob.close()
#
#         report_form.save()
#
#         return HttpResponseRedirect('/files/report')
#     else:
#         return render(request, 'report.html')
#
#
def get2(f: FileStorage):
    fs = GridFS(get_db())
    # 计算文件属性
    mimetype = filelib.mime(f.stream)
    sha1 = filelib.sha1(f.stream)
    md5 = filelib.md5(f.stream)
    arg = {'mimetype': mimetype, 'sha1': sha1, 'md5': md5}
    exist_fs = fs.find_one(arg)
    if exist_fs:
        return exist_fs._id, {'mimetype': exist_fs.mimetype, 'sha1': exist_fs.sha1, 'md5': exist_fs.md5}

    newfile = fs.new_file(content_type=mimetype, **arg)
    newfile.write(f.stream)  # f.stream.read()
    newfile.close()
    return newfile._id, arg


def create(**kwargs):
    model = {}
    for name, value in kwargs.items():
        setattr(model, name, value)


if __name__ == '__main__':
    unittest.main()
