import io

from flask import Blueprint, jsonify, render_template, send_file

from domain.index import IndexDomain

controller = Blueprint('INDEX_CONTROLLER', __name__)


@controller.route('/')
def index():
    return render_template("index.html")


@controller.route('/api/list')
def list():
    return jsonify(IndexDomain().list())


@controller.route('/img/<id>')
def img(id):
    blob, resource = IndexDomain().img(id)
    # im = Image.open(io.BytesIO(blob.blob.read()))
    return send_file(io.BytesIO(blob.blob.read()), mimetype="image/jpeg")


@controller.route('/detail/<id>')
def detail(id):
    # id = request.args.get("id")
    return jsonify(IndexDomain().detail(id))
