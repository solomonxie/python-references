# FLAKE8: NOQA
# $ uvicorn fastapi_poc.09_demo:app --reload
# $ curl 'http://127.0.0.1:8000/products?ids=1,2,3'
# $ open http://127.0.0.1:8000/docs
"""
Combines two datastores behind one endpoint: product metadata from MongoDB
merged with performance metrics from ClickHouse. A common shape for a
"catalog + analytics" API — see 07_clickhouse.py and 08_mongodb.py for each
piece on its own.
"""
import os
from fastapi import FastAPI
from pymongo import MongoClient
import clickhouse_connect

app = FastAPI()


def get_products_collection():
    password = os.getenv('MG_PASS', '')
    conn_str = f"mongodb://reader:{password}@localhost:27017/?directConnection=true"
    return MongoClient(conn_str)['my_database']['products']


def get_clickhouse_client():
    return clickhouse_connect.get_client(
        host='localhost', port=8123,
        username='default', password=os.getenv('CH_PASS', ''),
    )


@app.get('/products')
def list_products(ids: str, start_date: str = '2024-01-01', end_date: str = '2024-01-10'):
    id_list = [int(i) for i in ids.split(',') if i]

    # 1. Metadata from Mongo
    products = list(get_products_collection().find({'_id': {'$in': id_list}}))

    # 2. Metrics from ClickHouse
    sql = """
        SELECT product_id, date, downloads, revenue
        FROM product_performance
        WHERE product_id IN %(ids)s AND date BETWEEN %(start)s AND %(end)s
        ORDER BY date
    """
    params = {'ids': tuple(id_list), 'start': start_date, 'end': end_date}
    metrics = get_clickhouse_client().query(sql, params).named_results()

    metrics_by_product = {}
    for row in metrics:
        metrics_by_product.setdefault(row['product_id'], []).append(row)

    return [
        {**product, 'performance': metrics_by_product.get(product['_id'], [])}
        for product in products
    ]
