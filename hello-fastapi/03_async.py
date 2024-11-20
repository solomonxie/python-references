# $ uvicorn 03_async:app --reload
# $ curl http://127.0.0.1:8000

from typing import Union
from time import sleep

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    d = list(range(3))
    sleep(1)
    return {"Hello": str(d)}
