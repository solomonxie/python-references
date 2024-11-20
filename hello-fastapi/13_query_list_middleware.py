# $ uvicorn 13_query_list_middleware:app --reload
# $ curl 'http://127.0.0.1:8000/items?country=US,CA,WW'

from urllib.parse import urlencode

from fastapi import FastAPI, Query, Request
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()


class FlattenQueryListMiddleware(BaseHTTPMiddleware):
    """Rewrites `?country=US,CA,WW` into `?country=US&country=CA&country=WW`
    before routing, so handlers can keep using a plain `list[str] = Query(...)`
    instead of parsing comma-separated values themselves."""

    async def dispatch(self, request: Request, call_next):
        flattened = []
        for key, value in request.query_params.multi_items():
            flattened.extend((key, entry) for entry in value.split(","))
        request.scope["query_string"] = urlencode(flattened, doseq=True).encode("utf-8")
        return await call_next(request)


app.add_middleware(FlattenQueryListMiddleware)


@app.get("/items")
def list_items(country: list[str] = Query(default=[])):
    return {"country": country}
