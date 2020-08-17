from flask import Flask
from opentelemetry import trace
from opentelemetry.exporter import jaeger
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor

SETTINGS_NAME = "TRACING_SETTINGS"

def init(conf):
    trace.set_tracer_provider(TracerProvider())
    # https://opentelemetry-python.readthedocs.io/en/stable/exporter/jaeger/jaeger.html
    # create a JaegerSpanExporter
    jaeger_exporter = jaeger.JaegerSpanExporter(
        service_name=conf['service_name'],
        # configure agent
        agent_host_name=conf['agent_host_name'],
        agent_port=conf['agent_port'],
        # optional: configure also collector
        # collector_host_name='localhost',
        # collector_port=14268,
        # collector_endpoint='/api/traces?format=jaeger.thrift',
        # collector_protocol='http',
        # username=xxxx, # optional
        # password=xxxx, # optional
    )
    # Create a BatchExportSpanProcessor and add the exporter to it
    span_processor = BatchExportSpanProcessor(jaeger_exporter)
    # add to the tracer
    trace.get_tracer_provider().add_span_processor(span_processor)


def init_app(app: Flask):
    conf = app.config[SETTINGS_NAME]
    init(conf)


if __name__ == '__main__':
    init({
        'service_name': 'my-helloworld-service',
        'agent_host_name': '192.168.110.252',
        'agent_port': 6831
    })
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span('foo'):
        print('Hello world!')
