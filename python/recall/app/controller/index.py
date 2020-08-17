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
    return jsonify(ResourceDomain().list())


@controller.route('/upload', methods=['POST'])
def upload():
    for (k, f) in request.files.items():
        meta = mongolib.put(f)
        print(f.filename)
        print(request.form["title"])
        print(request.form["tags"])
        print(meta)
    return "newfile._id, {'mimetype': "", 'sha1': "", 'md5': newfile.md5}"


@controller.route('/img/<id>')
def img(id):
    resource = ResourceDomain().get(id)
    # im = Image.open(io.BytesIO(blob.blob.read()))
    file = mongolib.get(resource.blob_id)
    return send_file(io.BytesIO(file.read()), mimetype=file.content_type)


@controller.route('/detail/<id>')
def detail(id):
    # id = request.args.get("id")
    return jsonify(ResourceDomain().get(id))
