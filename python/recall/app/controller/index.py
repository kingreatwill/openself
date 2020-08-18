import io

from PIL import Image
from flask import Blueprint, jsonify, render_template, send_file, request
from flask_restful import reqparse

from core import mongolib, convlib, imagelib
from domain.resource import ResourceDomain

controller = Blueprint('INDEX_CONTROLLER', __name__)


@controller.route('/')
def index():
    return render_template('index.html')


# https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
@controller.route('/api/list/<int:index>', methods=['GET'])
@controller.route('/api/list/', methods=['GET'])
@controller.route('/api/list', methods=['GET'])
def list(index=1):
    result = ResourceDomain().list(index=index, **request.args)
    return jsonify(result)


@controller.route('/upload', methods=['POST'])
def upload():
    files = {}
    for (k, f) in request.files.items():
        files[f.filename.strip('"')] = f
    arg = {'title': request.values.get('title', default=''), 'tags': request.values.get('tags', default='')}
    result = ResourceDomain().create(files, **arg)
    return jsonify(result)


@controller.route('/update/<id>', methods=['POST'])
def update(id):
    # title 和 tags
    result = ResourceDomain().update(id, **request.form)
    return jsonify(result)


# http://127.0.0.1:5000/img/5f3b471842b7e25d1aeac4c4?width=500&height=100&resample=5&quality=95&force=resize
@controller.route('/img/<id>', methods=['GET'])
def img(id):
    parser = reqparse.RequestParser()
    parser.add_argument('format', type=str, help='文件后缀')
    parser.add_argument('width', type=int, default=0, help='图片宽')
    parser.add_argument('height', type=int, default=0, help='图片高')
    parser.add_argument('force', type=str, default="resize", help='处理类型(resize,中心裁剪：crop_center:1)')
    parser.add_argument('resample', type=int, default=1, help='重新采样使用的方法')
    parser.add_argument('quality', type=int, default=100, help='图片质量')
    args = parser.parse_args()

    resource = ResourceDomain().get(id)
    if imagelib.is_img(resource.extension):
        file = mongolib.get(resource.blob_id)
        if not args["format"]:
            args["format"] = file.extension
        byte_io = imagelib.thumbnail(io.BytesIO(file.read()), **args)
        return send_file(byte_io, mimetype=imagelib.to_mimetype(args["format"]))  # mimetype=file.content_type
    return "Error image type."


# 获取源文件(非下载);
@controller.route('/raw/<id>', methods=['GET'])
def raw(id):
    resource = ResourceDomain().get(id)
    # im = Image.open(io.BytesIO(blob.blob.read()))
    file = mongolib.get(resource.blob_id)
    return send_file(io.BytesIO(file.read()), mimetype=file.content_type)


# 获取源文件(直接下载);
@controller.route('/blob/<id>', methods=['GET'])
def blob(id):
    resource = ResourceDomain().get(id)
    file = mongolib.get(resource.blob_id)
    return send_file(io.BytesIO(file.read()), mimetype=file.content_type, as_attachment=True,
                     attachment_filename=resource.filename, cache_timeout=0)


@controller.route('/detail/<id>', methods=['GET'])
def detail(id):
    # id = request.args.get("id")
    return jsonify(ResourceDomain().get(id))
