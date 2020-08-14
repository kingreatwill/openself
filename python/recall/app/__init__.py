from flask import Flask, Response, jsonify
from controller import index, admin
from .models import db
from core.json import RecallJSONEncoder


def create_app(config):
    app = Flask(__name__)
    # http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/
    app.config['MONGODB_SETTINGS'] = {
        'db': 'recall',
        'alias': 'recall-db-alias',
        'host': '127.0.0.1',
        'port': 27017
    }
    db.init_app(app)
    app.json_encoder = RecallJSONEncoder
    # app.response_class = RecallResponse
    app.register_blueprint(index.controller, url_prefix="/")
    app.register_blueprint(admin.controller, url_prefix="/admin")
    return app
