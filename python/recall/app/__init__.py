from flask import Flask
from controller import index, admin
from models import db
from core import tracing
from core.jsonlib import RecallJSONEncoder
from opentelemetry.instrumentation.pymongo import PymongoInstrumentor
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from prometheus_flask_exporter import PrometheusMetrics

def create_app(config):
    app = Flask(__name__)
    # http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/
    # mongodb config
    app.config['MONGODB_SETTINGS'] = {
        'db': 'recall',
        'host': '127.0.0.1',
        'port': 27017
    }
    # tracing config
    app.config[tracing.SETTINGS_NAME] = {
        'service_name': 'my-helloworld-service',
        'agent_host_name': '192.168.110.252',
        'agent_port': 6831
    }
    # metrics
    metrics = PrometheusMetrics(app)
    # Tracing
    tracing.init_app(app)
    # OpenTelemetry pymongo Instrumentation
    PymongoInstrumentor().instrument()
    # OpenTelemetry WSGI Instrumentation
    # https://opentelemetry-python.readthedocs.io/en/stable/instrumentation/wsgi/wsgi.html#usage-flask
    # app.wsgi_app = OpenTelemetryMiddleware(app.wsgi_app)
    # OpenTelemetry Flask Instrumentation
    FlaskInstrumentor().instrument_app(app)
    # 初始化数据库配置
    db.init_app(app)
    app.json_encoder = RecallJSONEncoder
    # app.response_class = RecallResponse
    app.register_blueprint(index.controller, url_prefix="/")
    app.register_blueprint(admin.controller, url_prefix="/admin")
    return app
