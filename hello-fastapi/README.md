# FastAPI POC

Small, standalone FastAPI examples, roughly ordered from basics to more
realistic setups. Each file has its `uvicorn`/`curl` commands as a comment
at the top — cd into this folder and run it, e.g.:

```sh
cd hello-fastapi
pip install -r requirements.txt
uvicorn 01_helloworld:app --reload
curl http://127.0.0.1:8000/items/5?q=somequery
open http://127.0.0.1:8000/docs   # interactive Swagger UI
```

| File | Demonstrates |
|---|---|
| `01_helloworld.py` | Minimal app, path/query params |
| `02_io_models.py` | Pydantic request/response models |
| `03_async.py` | `async def` path operations |
| `04_middlewares.py` | Custom middleware (timing header) |
| `05_advanced_middlewares.py` | Starlette's lower-level middleware API |
| `06_auth.py` | HTTP Basic auth via a Starlette `AuthenticationBackend` |
| `07_clickhouse.py` | Querying ClickHouse from a route |
| `08_mongodb.py` | Querying MongoDB from a route |
| `09_demo.py` | Combining Mongo (metadata) + ClickHouse (metrics) behind one endpoint |
| `10_router.py` | Splitting routes across an `APIRouter` |

`07`–`09` expect a ClickHouse/MongoDB instance reachable at `localhost` (see
`CH_PASS`/`MG_PASS` env vars in each file) — they're meant to be read as
examples rather than run out of the box.
