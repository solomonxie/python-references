# FLAKE8: NOQA
# $ uvicorn fastapi_poc.10_router:app --reload
# $ curl http://127.0.0.1:8000/items/5?q=somequery
# $ open http://127.0.0.1:8000/docs

import os
import yaml
from fastapi import FastAPI
from fastapi import APIRouter

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


app = FastAPI()
app.include_router(router)
