# REF: https://www.starlette.io/middleware/
# $ uvicorn 05_advanced_middlewares:app --reload
# $ curl http://127.0.0.1:8000

from typing import Union
from time import sleep, time

from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


class MyMiddlewareClass1(BaseHTTPMiddleware):

    def __init__(self, app):
        # Inited when app loaded into memory
        super().__init__(app)

    async def dispatch(self, request, call_next):
        start_time = time()
        response = await call_next(request)
        process_time = time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response


class MyMiddlewareClass2(BaseHTTPMiddleware):

    def __init__(self, app):
        # Inited when app loaded into memory
        super().__init__(app)

    async def dispatch(self, request, call_next):
        start_time = time()
        response = await call_next(request)
        process_time = time() - start_time
        response.headers["X-Process-Time2"] = str(process_time)
        return response


app = FastAPI()
app.add_middleware(MyMiddlewareClass1)
app.add_middleware(MyMiddlewareClass2)  # FILO

@app.get("/")
async def read_root():
    d = list(range(3))
    d = list(range(10))
    return {"Hello": str(d)}
