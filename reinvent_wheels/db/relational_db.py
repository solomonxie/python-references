
import os
import sqlalchemy
import sqlalchemy.exc
from time import time
from time import sleep
from hashlib import md5
# from telnetlib import Telnet
# from urllib.parse import urlparse
from collections import OrderedDict

from sqlalchemy.sql import text
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker, scoped_session
# from sqlalchemy.exc import ProgrammingError, OperationalError, TimeoutError

import logging
logger = logging.getLogger(__name__)

from reinvent_wheels.structures.insensitive_dict import CaseInsensitiveDict
from reinvent_wheels.builtin.concurrency_utils import ThreadPoolManager


class BaseRelationalDBConnector:
    DIALECT = ''
    PARAM_BRACKET = True

    def __init__(self, **kwargs):
        self.debug = {'sql_durations': [], 'errors': []}
        self.specs = kwargs
        self.conn_str = self.get_conn_str(**kwargs)
        self.engine = self.get_engine(**kwargs)
        self.qtag = kwargs.get('qtag')
        self.retry_count = int(kwargs.get('retry') or 3)
        self.retry_interval = float(kwargs.get('retry_interval') or 1)

    def get_conn_str(self, **kwargs):
        raise NotImplementedError()

    def get_connect_args(self, **kwargs) -> dict:
        return {}

    @property
    def location(self):
        return repr(self.engine.url)

    def get_extra_engine_args(self, **kwargs) -> dict:
        return {}

    def get_engine(self, **kwargs):
        echo = bool(os.getenv('DEBUG') is True and str(os.getenv('DB_ECHO')).lower() != 'false')
        args = {
            'echo': echo,
            'poolclass': self.specs.get('pool_cls') or QueuePool,
            'pool_recycle': 900,  # timeout of waiting queue spot
            'pool_size': 256,
            'connect_args': self.get_connect_args(**self.specs),
            **self.get_extra_engine_args(**kwargs),
        }
        engine = sqlalchemy.create_engine(self.conn_str, **args)
        conn_str = repr(engine.url)  # `repr(engine.url)` hides password
        logger.debug(f'DB Engine will connect to: {conn_str}')
        self.debug['engine_url'] = conn_str
        self.debug['engine_args'] = str(args)
        return engine

    def get_session(self):
        # self.test_connect()  # Should test in upper layer, here it'll affect UT mocking
        session = scoped_session(sessionmaker(bind=self.engine, autocommit=False))
        return session

    def _send_sql(self, session, sql: str, params: dict = None, **kwargs) -> list:
        if not sql:
            return []
        try:
            session.begin()
            q = session.execute(text(sql), params)
            rows = q.fetchall() if q.returns_rows else []
            session.commit()
        except Exception as e:
            self.debug['errors'].append(str(e))
            logger.exception(e)
            session.rollback()
            raise e
        # params = OrderedDict({k: params[k] for k in sorted(params.keys())}) if params else ''
        return rows

    def post_process_rows(self, rows, **kwargs):
        for i in range(len(rows)):
            if kwargs.get('dict_row') is not False:
                rows[i] = dict(rows[i])
            if kwargs.get('insensitive_dict') is not False:
                rows[i] = CaseInsensitiveDict(rows[i])
        return rows

    def run(self, *args, **kwargs):
        return self.run_sql(*args, **kwargs)

    def q(self, *args, **kwargs):
        return self.run_sql(*args, **kwargs)

    def query(self, *args, **kwargs):
        return self.run_sql(*args, **kwargs)

    def run_sql(self, sql: str, params: dict = None, **kwargs):
        if not sql:
            return []
        start = time()
        session = self.get_session()
        qtag = kwargs.get('qtag') or self.qtag or self.generate_qtag(sql, params)
        sql += f'\n /* qtag: {qtag} */ \n'
        rows = []
        for i in range(self.retry_count):
            try:
                rows = self._send_sql(session, sql, params, **kwargs)
                break
            except (sqlalchemy.exc.ProgrammingError, ) as e:
                raise e
            except Exception as e:
                if i + 1 >= self.retry_count:
                    raise e
                logger.debug(e)
                logger.warning(f'Retrying sql [{qtag}]...')
                sleep(self.retry_interval)
        rows = self.post_process_rows(rows, **kwargs)
        self.debug['sql_durations'].append(f'{time() - start:.3f}')
        return rows

    def export(self, *args, **kwargs):
        return self.run_sql_dump(*args, **kwargs)

    def dump(self, *args, **kwargs):
        return self.run_sql_dump(*args, **kwargs)

    def run_sql_dump(self, local_path: str, sql: str, params: dict = None, **kwargs):
        pass

    def run_more_sqls(self, sql_map: dict, concurrency: int = 5, **kwargs) -> dict:
        logger.debug(f'Running [{len(sql_map)}] SQLs with {concurrency} workers...')
        pool = ThreadPoolManager(concurrency=concurrency)
        for k, (sql, params) in sql_map.items():
            pool.add_task(k, self.run_sql, sql, params, **kwargs)
        result_map = pool.get_result()
        return result_map

    def dump_files(self, sql_map: dict, file_map: dict, concurrency: int = 3, **kwargs) -> dict:
        logger.debug(f'Dumping SQL data [{len(sql_map)}] with {concurrency} workers...')
        pool = ThreadPoolManager(concurrency=concurrency)
        for k, (sql, params) in sql_map.items():
            pool.add_task(k, self.run_sql_dump, file_map[k], sql, params, **kwargs)
        result_map = pool.get_result()
        return result_map

    def dump_files_1_thread(self, sql_map: dict, file_map: dict, **kwargs) -> dict:
        logger.debug(f'Dumping SQL data [{len(sql_map)}]...')
        local_file_map = {}
        for k, (sql, params) in sql_map.items():
            # MAIN SQL:
            local_file_map[k] = self.run_sql_dump(file_map[k], sql, params, **kwargs)
        return local_file_map

    def get_row_count(self, local_path: str) -> int:
        rcount = 0
        try:
            rcount = self.run(f""" SELECT COUNT(1) AS c FROM '{local_path}'; """)[0]['C']
        except Exception as e:
            logger.warning(f'Failed to read file: {local_path} {e}')
        return rcount

    def generate_qtag(self, sql: str, params: dict = None):
        params = OrderedDict({k: params[k] for k in sorted(params.keys())}) if params else ''
        qtag = md5(f'{sql}\n{params}'.encode('utf-8')).hexdigest()
        return qtag

    def test_connect(self):
        logger.debug(f'Testing DB Connection with: {repr(self.engine.url)}')
        start = time()
        self.engine.connect()
        self.debug['connection_speed'] = int(time() - start)
        logger.debug(f'Success: DB Connected with: {repr(self.engine.url)}')
