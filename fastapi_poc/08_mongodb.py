# $ uvicorn fastapi_poc.08_mongodb:app --reload
# $ curl http://127.0.0.1:8000/
# $ open http://127.0.0.1:8000/docs

import os
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()


@app.get("/")
def read_mongo():
    password = os.getenv('MG_PASS', '')
    conn_str = f"mongodb://reader:{password}@localhost:27017/?directConnection=true"
    client = MongoClient(conn_str)

    db = client['my_database']
    collection = db['my_collection']
    row = collection.find_one({"month": "2020-08"})
    return row
