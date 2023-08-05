from sqlbatis import Engin, DBEngin
from .log_support import save_log, save_key_seq_log

# Don't remove. Import for not repetitive implementation
from sqlbatis.db import init_db as supper_init_db, insert, save as save_select_key, execute, batch_insert, batch_execute, get, query, query_one, \
    query_page, select, select_one, select_page, do_execute, do_get, do_query, do_query_one, do_query_page, do_select, do_select_one, do_select_page

_DB_CTX = None


def init_db(user='root', password='', database='test', host='127.0.0.1', port=3306, pool_size=0, show_sql=False, **kwargs):
    supper_init_db(user=user, password=password, database=database, host=host, port=port, engin=Engin.POSTGRESQL, pool_size=pool_size, \
                   show_sql=show_sql, **kwargs)


def save(table: str, **kwargs):
    """
    Insert data into table, return primary key.
    :param table: table
    :param kwargs:
    :return: Primary key
    """
    save_log(table, **kwargs)
    return save_key_seq(f'{table}_id_seq', table, **kwargs)


def save_key_seq(key_seq: str, table: str, **kwargs):
    """
    Insert data into table, return primary key.
    :param key_seq: primary key sequnece
    :param table: table
    :param kwargs:
    :return: Primary key
    """
    save_key_seq_log(key_seq, table, **kwargs)
    return save_select_key(DBEngin.get_select_key(key_seq=key_seq), table, **kwargs)


