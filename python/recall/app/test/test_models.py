import unittest
from mongoengine import connect
from core import filelib
import models


class TestCluster(unittest.TestCase):
    def setUp(self):
        connect(db='recall', alias="recall-db-alias", host='127.0.0.1', port=27017)
        # 如需验证和指定主机名 http://docs.mongoengine.org/guide/connecting.html#connecting-to-mongodb
        # connect('blog', host='127.0.0.1', port=27017, username='root', password='1234')
        # http://docs.mongoengine.org/guide/gridfs.html#writing
    def test_save(self):
        blob = models.ResourceBlob()
        with open('xxx.jpg', 'rb') as fd:
            blob.blob.put(fd, content_type='image/jpeg')
            blob.hash = filelib.sha1(fd)
            blob.md5 = filelib.md5(fd)
        basic = models.Resource(blob_id=blob.blob_id, title="filename", tags=["ai", "bigdata"])
        blob.save()
        basic.save()

    def test_update(self):
        # 返回所有符合查询条件的结果的文档对象列表
        rs = models.Resource.objects(title="filename").first()
        # 更新查询到的文档:
        # rs.title = "jw"
        rs.tags.append("tag")
        rs.update()

    def test_select(self):
        # # 返回集合里的所有文档对象的列表
        all_blob = models.ResourceBlob.objects.all()
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
