import os
import random
from time import time
from urllib.parse import quote

from reinvent_wheels.builtin.concurrency_utils import ThreadPoolManager

import snowflake.connector

import logging
logger = logging.getLogger(__name__)


class SnowflakeConnector:
    DIALECT = 'snowflake'
    PARAM_BRACKET = False

    def __init__(self, **kwargs):
        self.specs = kwargs
        self.req_id = kwargs.pop('req_id', None)
        self.conn_args = self.get_conn_args(**kwargs)
        self.retry_count = int(kwargs.get('retry') or 3)
        self.retry_interval = float(kwargs.get('retry_interval') or 1)
        self.debug = {'sql_durations': {}, 'errors': []}

    def get_conn_args(self, **kwargs) -> dict:
        _warehouses = str(kwargs.get('warehouse') or os.getenv('SNOWFLAKE_WAREHOUSE')).split('|')
        args = {
            'user': quote(kwargs.get('username') or os.getenv('SNOWFLAKE_USERNAME')),
            'password': quote(kwargs.get('password') or os.getenv('SNOWFLAKE_PASSWORD') or ''),
            'account': kwargs.get('account') or os.getenv('SNOWFLAKE_ACCOUNT'),
            'warehouse': random.choice(_warehouses),
            'database': kwargs.get('db') or os.getenv('SNOWFLAKE_DATABASE'),
            # 'schema': '',
        }

        return args

    def query(self, sql: str, params: dict = None, **kwargs):
        if not sql:
            return []
        start = time()
        if self.req_id:
            params = {'req_id': str(self.req_id), **(params or {})}
            sql = sql + '/*req_id: %(req_id)s*/ \n'
        with snowflake.connector.connect(**self.conn_args) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, params)
            colnames = [col[0] for col in cursor.description]
            rows = []
            for row in cursor.fetchall():
                x = dict(zip(colnames, row))
                rows.append(x)
        qtag = kwargs.get('qtag') or (sql[:10] + '...')
        self.debug['sql_durations'][qtag] = round(time() - start, 2)
        return rows

    def wrap_sql_dump(self, sql: str, path: str, **kwargs) -> str:
        # REF: https://docs.snowflake.com/en/sql-reference/sql/copy-into-location.html
        if not sql:
            return ''
        quoting = ""
        if kwargs.get('quoting'):
            quoting = " FIELD_OPTIONALLY_ENCLOSED_BY = '{quoting}' "
        formats = {
            ".parquet": """
                TYPE ='PARQUET' COMPRESSION='AUTO' TRIM_SPACE=TRUE
            """,
            ".csv": f"""
                TYPE ='CSV'
                COMPRESSION=NONE
                EMPTY_FIELD_AS_NULL=FALSE
                NULL_IF=''
                RECORD_DELIMITER = '\n'
                FIELD_DELIMITER = ','
                {quoting}
            """,
            ".csv.gz": f"""
                TYPE ='CSV'
                COMPRESSION='GZIP'
                EMPTY_FIELD_AS_NULL=FALSE
                NULL_IF=''
                RECORD_DELIMITER = '\n'
                FIELD_DELIMITER = ','
                {quoting}
            """,
            ".json": """
                TYPE ='JSON' COMPRESSION='AUTO' TRIM_SPACE=TRUE
            """,
            ".json.gz": """
                TYPE ='JSON' COMPRESSION='gzip' TRIM_SPACE=TRUE
            """,
        }
        fmt = ([v for k, v in formats.items() if path.endswith(k)] + [formats['.csv']])[0]
        cmd = f"""
            COPY INTO '{path}' FROM (
            {sql}
            ) FILE_FORMAT = ({fmt})
            SINGLE = TRUE OVERWRITE = TRUE HEADER = TRUE MAX_FILE_SIZE = 5368709120  --5GB
        """
        return cmd

    def export(self, local_path: str, sql: str, params: dict = None, **kwargs):
        start = time()
        remote_path = '@~/unload' + local_path  # FIXME
        local_dir = os.path.dirname(local_path)
        os.makedirs(local_dir, exist_ok=True)
        cmd = self.wrap_sql_dump(sql, remote_path, **kwargs)
        result = self.query(cmd, params, **kwargs)
        logger.debug(f'Prepared data for [{remote_path}] in {time() - start}s: {result}')
        rows_len = int(result[0]['rows_unloaded']) if result and len(result) > 0 else 0
        if rows_len < 1 and kwargs.get('raise_on_empty'):
            raise ValueError(f'Data empty for: {local_path}')
        if rows_len < 1:
            return None
        cmd = f"GET '{remote_path}' 'file://{local_dir}/' ;"
        self.query(cmd, None, **kwargs)
        cmd = f"REMOVE '{remote_path}' ;"
        self.query(cmd, None, **kwargs)
        duration = round(time() - start, 2)
        qtag = kwargs.get('qtag') or (sql[:10] + '...')
        self.debug['sql_durations'][qtag] = duration
        logger.debug(f'Dumped SQL [{qtag}] in {duration}s at {local_path}')
        return rows_len

    def dump_files(self, sql_map: dict, file_map: dict, concurrency: int = 3, **kwargs) -> dict:
        logger.debug(f'Dumping SQL data [{len(sql_map)}] with {concurrency} workers...')
        pool = ThreadPoolManager(concurrency=concurrency)
        for k, (sql, params) in sql_map.items():
            pool.add_task(k, self.export, file_map[k], sql, params, **kwargs)
        result_map = pool.get_result()
        return result_map

    def dump_files_1_thread(self, sql_map: dict, file_map: dict, **kwargs) -> dict:
        logger.debug(f'Dumping SQL data [{len(sql_map)}]...')
        local_file_map = {}
        for k, (sql, params) in sql_map.items():
            # MAIN SQL:
            local_file_map[k] = self.export(file_map[k], sql, params, **kwargs)
        return local_file_map

    def query_more(self, sql_map: dict, concurrency: int = 5, **kwargs) -> dict:
        logger.debug(f'Running [{len(sql_map)}] SQLs with {concurrency} workers...')
        pool = ThreadPoolManager(concurrency=concurrency)
        for k, (sql, params) in sql_map.items():
            pool.add_task(k, self.query, sql, params, **kwargs)
        result_map = pool.get_result()
        return result_map


def main():
    conn = SnowflakeConnector()
    sql = 'select * from my_schema.my_table where id IN (%(ids)s)'
    params = {'ids': tuple([1, 2, 3])}
    rows = conn.query(sql, params)
    print(rows)


if __name__ == '__main__':
    main()
