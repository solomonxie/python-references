# Python References

A personal sandbox for trying out Python: proof-of-concept demos of
libraries/frameworks, and from-scratch reimplementations ("reinvented
wheels") of things a 3rd party package would normally provide.

## Layout

- `learn/` — Algorithms, data structures, design patterns, and language features, one focused script each
- `reinvent_wheels/` — Minimal-dependency reimplementations: thread pool, retry decorator, DB connectors, case-insensitive dict, etc.
- `hello-fastapi/` — FastAPI examples: routing, middleware, auth, and querying Mongo/ClickHouse
- `flask_poc/` — Flask, for comparison against the FastAPI examples
- `rabbitmq_poc/` — RabbitMQ producer/consumer basics, plus a small reusable task-queue helper
- `opentelemetry_poc/` — Tracing/metrics instrumentation on a Flask app
- `cdk-aws-poc/` — Minimal AWS CDK stack (Lambda behind an HTTP API)
- `sam-aws-poc/` — Same idea via AWS SAM

Each subfolder has its own README with setup/run instructions where that's
non-obvious from the code.

## Getting started

- Each subfolder is meant to be self-contained: `cd` into it, check its README, and install its `requirements.txt` (usually in a fresh virtualenv)
- Scripts are numbered where order matters (e.g. `hello-fastapi/01_helloworld.py`, `02_io_models.py`, ...) — read/run them in that order to follow the progression
- Nothing here is production code; it's meant for reading and experimenting, not importing into other projects
