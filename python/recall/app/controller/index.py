import io

from flask import Blueprint, jsonify, render_template, send_file, request
from gridfs import GridFS
from mongoengine import get_db

from core import mongolib, filelib
from domain.resource import ResourceDomain

controller = Blueprint('INDEX_CONTROLLER', __name__)


@controller.route('/')
def index():
    return render_template("index.html")


@controller.route('/api/list')
def list():
    print(request.args)
    result = ResourceDomain().list()
    return jsonify(result)


@controller.route('/upload', methods=['POST'])
def upload():
    files = {}
    for (k, f) in request.files.items():
        files[f.filename.strip('"')] = f
    arg = {"title": request.form["title"], "tags": request.form["tags"]}
    result = ResourceDomain().create(files, **arg)
    return jsonify(result)


@controller.route('/raw/<id>')
def raw(id):
    resource = ResourceDomain().get(id)
    # im = Image.open(io.BytesIO(blob.blob.read()))
    file = mongolib.get(resource.blob_id)
    return send_file(io.BytesIO(file.read()), mimetype=file.content_type)


# 获取源文件(直接下载);
@controller.route('/blob/<id>')
def blob(id):
    resource = ResourceDomain().get(id)
    file = mongolib.get(resource.blob_id)
    return send_file(io.BytesIO(file.read()), mimetype=file.content_type, as_attachment=True,
                     attachment_filename=resource.filename)


@controller.route('/detail/<id>')
def detail(id):
    # id = request.args.get("id")
    return jsonify(ResourceDomain().get(id))
