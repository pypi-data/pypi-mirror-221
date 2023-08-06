from .engin import PostgresEngin

# Don't remove. Import for not repetitive implementation
from sqlbatis.sql_support import require_limit, dynamic_sql


def page_sql_args(sql: str, page_num=1, page_size=10, *args):
    start = (page_num - 1) * page_size
    return PostgresEngin.page_sql_args(require_limit, sql, start, page_size, *args)

