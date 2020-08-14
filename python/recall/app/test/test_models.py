import unittest

# from gridfs import GridFS # fs = GridFS()
from mongoengine import connect,FileField
from core import filelib
import models


class TestModels(unittest.TestCase):
    def setUp(self):
        connect(db='recall', alias="recall-db-alias", host='127.0.0.1', port=27017)
        # 如需验证和指定主机名 http://docs.mongoengine.org/guide/connecting.html#connecting-to-mongodb
        # connect('blog', host='127.0.0.1', port=27017, username='root', password='1234')
        # http://docs.mongoengine.org/guide/gridfs.html#writing

    def test_model(self):
        blob = models.Resource()
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
                blob.blob.put(fd, content_type=content_type)
                blob.save()
            blob_id = exist_blob.blob_id
        # 文件元信息保存;
        basic = models.Resource(blob_id=blob_id, title="filename", tags=["ai", "bigdata"])
        basic.save()

    def test_update(self):
        # 返回所有符合查询条件的结果的文档对象列表
        rs = models.Resource.objects(title="filename").first()
        # 更新查询到的文档:http://docs.mongoengine.org/guide/querying.html?highlight=update#atomic-updates
        rs.update(push__tags="tag_end")  # 追加，不能是数组
        # rs.update(push__tags__0=["tag"]) # 指定位置追加，可以多个
        # models.Resource.objects(tags='tag_end').update(set__tags__S='mongodb') # 更新tag_end = mongodb，只更新第一个位置的
        rs.update(tags=["fin_tag"])
        # rs.update(set__tags=["fin_tag","xx"]) # 同上

    def test_select(self):
        # # 返回集合里的所有文档对象的列表
        f= models.ResourceBlob.objects.all().first()
        b = f.blob.get()
        all_blob = models.ResourceBlob.objects.all()
        print(all_blob.to_json())
        print(all_blob.as_pymongo())
        # Order by ascending date first, then descending title
        #blogs = BlogPost.objects().order_by('+date', '-title')
        # 5 users, starting from the 11th user found
        #users = User.objects[10:15]  # limit() and skip()
        # comments - skip 5, limit 10
        #Page.objects.fields(slice__comments=[5, 10])
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


if __name__ == '__main__':
    unittest.main()
