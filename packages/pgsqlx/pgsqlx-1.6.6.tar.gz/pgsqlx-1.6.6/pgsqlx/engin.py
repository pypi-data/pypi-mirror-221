import re
from .log_support import logger
from functools import lru_cache
from .constant import CACHE_SIZE
from sqlbatis.engin import Engin, DBError


class PostgresEngin(Engin):
    def __init__(self, engin):
        super().__init__(engin)

    @classmethod
    def init(cls, name='PostgreSQL'):
        super().init(name)

    @staticmethod
    def _page_sql_args(require_limit, sql: str, start, page_size, *args):
        if require_limit(sql):
            sql = '{} LIMIT ? OFFSET ?'.format(sql)
        args = [*args, page_size, start]
        return sql, args

    @staticmethod
    def _get_select_key(key_seq: str = None, table: str = None, sql: str = None):
        if not key_seq:
            if table:
                key_seq = PostgresEngin._build_key_seq(table)
            else:
                if sql:
                    key_seq = PostgresEngin._get_key_seq_from_sql(sql)
                else:
                    raise DBError("Get PostgreSQL select key fail, all of 'key_seq', 'table', 'sql' are None")
        return f"SELECT currval('{key_seq}')"


    @staticmethod
    def _build_key_seq(table: str):
        return f'{table}_id_seq'

    @staticmethod
    @lru_cache(maxsize=CACHE_SIZE)
    def _get_key_seq_from_sql(sql: str):
        table = re.search('(?<=into )\w+', sql, re.I)
        key_seq = PostgresEngin._build_key_seq(table.group())
        logger.warning("'key_seq' is None, will use default '{}' from sql.".format(key_seq))
        return key_seq

