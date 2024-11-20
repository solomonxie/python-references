# REF: https://fastapi.tiangolo.com/tutorial/middleware/
# $ uvicorn 04_middlewares:app --reload

from typing import Union
from time import sleep, time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def my_req_resp_mid2(request: Request, call_next):
    start_time = time()
    response = await call_next(request)
    process_time = time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.middleware("http")
async def my_req_resp_mid1(request: Request, call_next):
    start_time = time()
    response = await call_next(request)
    process_time = time() - start_time
    response.headers["X-Process-Time2"] = str(process_time)
    return response


@app.get("/")
async def read_root():
    d = list(range(3))
    d = list(range(10))
    return {"Hello": str(d)}
