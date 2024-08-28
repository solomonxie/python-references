# OpenTelemetry POC

A tiny Flask "dice roller" instrumented with OpenTelemetry: a custom span
per request plus a counter metric, following the [official OTel Python
getting-started guide](https://opentelemetry.io/docs/languages/python/getting-started/).

```sh
cd hello-opentelemetry
pip install -r requirements.txt
opentelemetry-bootstrap -a install   # installs auto-instrumentation for Flask etc.

opentelemetry-instrument --traces_exporter console --metrics_exporter console \
    flask --app app run

curl 'http://127.0.0.1:5000/rolldice?player=alice'
```

Traces and metrics print to the console by default; point
`--traces_exporter otlp --metrics_exporter otlp` (with `OTEL_EXPORTER_OTLP_ENDPOINT`
set) at a real collector to see them somewhere like Jaeger or Grafana instead.
