# Reinvent Wheels

Small, dependency-light reimplementations of things a 3rd party package
would normally give you — thread pools, retry decorators, DB connection
wrappers, case-insensitive dicts, etc. The point is understanding how the
"wheel" works, not producing something production-grade.

**Rule of thumb:** prefer the standard library over a 3rd party package;
only use one when it's the thing actually being demoed (e.g. `sqlalchemy`,
`snowflake-connector-python`).

## Structure

```
reinvent_wheels/
├── builtin/
│   ├── concurrency_utils.py   # ThreadPoolManager — a tiny thread pool built on threading+queue
│   └── error_utils.py         # retry — a minimal retry decorator
├── network/
│   └── socket_utils.py        # get_safe_hostname
├── db/
│   ├── relational_db.py       # BaseRelationalDBConnector — SQLAlchemy-based, retry + concurrent queries
│   ├── snowflake_helper.py    # SnowflakeConnector — query + bulk export to file
│   ├── mongo.py               # (stub)
│   └── redis_helper.py        # (stub)
├── structures/
│   ├── api_exceptions.py      # (code, http_status) constants + exception classes for an API layer
│   ├── data_models.py         # EasyDataclass — a dataclass base with lenient __init__
│   └── insensitive_dict.py    # CaseInsensitiveDict, adapted from `requests` (Apache 2.0)
├── cache/, cloud/, graphic/, parser/   # (stubs — not implemented yet)
```

## Usage

Import from the package root, e.g.:

```python
from reinvent_wheels.builtin.concurrency_utils import ThreadPoolManager
from reinvent_wheels.structures.insensitive_dict import CaseInsensitiveDict
```

## Contribution

- Keep each file runnable/testable on its own — no hidden dependency on a
  specific external service being configured.
- If a file needs credentials to actually connect somewhere (DB, cloud API),
  read them from environment variables with a sensible local-dev default,
  never hardcode them.
