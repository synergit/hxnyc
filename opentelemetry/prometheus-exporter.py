from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.prometheus import PrometheusMetricsExporter
from opentelemetry.sdk.metrics import Counter, Meter
from prometheus_client import start_http_server

# Start Prometheus client
start_http_server(port=8080, addr="localhost")
# Meter is responsible for creating and recording metrics
# mp = metrics.DefaultMeterProvider()
# metrics.set_meter_provider(mp)
metrics.set_meter_provider(MeterProvider())
# metrics.set_meter_provider(global.GetMeter(name, version))
meter = metrics.get_meter(__name__)
# exporter to export metrics to Prometheus
prefix = "HXNYC"
exporter = PrometheusMetricsExporter(prefix)
# Starts the collect/export pipeline for metrics
metrics.get_meter_provider().start_pipeline(meter, exporter, 5)
counter = meter.create_counter(
# counter = meter.create_metric(
    "requests",
    "number of requests",
    "requests",
    int,
    # Counter,
    # ("environment",),
)

# Labels are used to identify key-values that are associated with a specific
# metric that you want to record. These are useful for pre-aggregation and can
# be used to store custom dimensions pertaining to a metric
labels = {"environment": "staging"}

counter.add(25, labels)
input("Press any key to exit...")