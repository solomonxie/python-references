# $ uvicorn 07_clickhouse:app --reload
# $ curl http://127.0.0.1:8000/
# $ curl 'http://127.0.0.1:8000/report?start_date=2024-01-01&end_date=2024-01-10&countries=US'
# $ open http://127.0.0.1:8000/docs

import os
import clickhouse_connect
from fastapi import FastAPI

app = FastAPI()


def get_client():
    return clickhouse_connect.get_client(
        host='localhost', port=8123,
        username='default', password=os.getenv('CH_PASS', ''),
    )


@app.get("/")
def read_clickhouse():
    client = get_client()
    return client.query('SELECT * FROM sales_estimates LIMIT 2').named_results()


@app.get("/report")
def read_report(start_date: str, end_date: str, countries: str, granularity: str = 'daily'):
    """A slightly more realistic query: parameterized, filtering on a date
    range plus a variable-length IN list built from a comma-separated arg."""
    client = get_client()
    sql = """
        SELECT product_id, date, country_code, downloads, revenue
        FROM product_performance
        WHERE granularity = %(granularity)s
          AND date BETWEEN %(start)s AND %(end)s
          AND country_code IN %(countries)s
        ORDER BY date
    """
    params = {
        'granularity': granularity,
        'start': start_date, 'end': end_date,
        'countries': tuple(countries.split(',')),
    }
    return list(client.query(sql, params).named_results())
