from .engin import PostgresEngin
from . import sql_support
from .log_support import save_log, save_key_seq_log, do_page_log, page_log

# Don't remove. Import for not repetitive implementation
from sqlbatis.db import insert, save as save_select_key, execute, batch_insert, batch_execute, get, query, query_one, select, select_one,\
    do_execute, do_get, do_query, do_query_one, do_select, do_select_one


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
    return save_select_key(PostgresEngin.get_select_key(key_seq=key_seq), table, **kwargs)



def query_page(sql: str, page_num=1, page_size=10, *args, **kwargs):
    """
    Execute select SQL and return list or empty list if no result. Automatically add 'limit ?,?' after sql statement if not.
    sql: SELECT * FROM user WHERE name=? and age=?  -->  args: ('张三', 20)
         SELECT * FROM user WHERE name=:name and age=:age  -->  kwargs: ('张三', 20) --> kwargs: {'name': '张三', 'age': 20}
    """
    page_log('query_page', sql, page_num, page_size, *args, **kwargs)
    sql, args = sql_support.dynamic_sql(sql, *args, **kwargs)
    return do_query_page(sql, page_num, page_size, *args)


def select_page(sql: str, page_num=1, page_size=10, *args, **kwargs):
    """
    Execute select SQL and return list(tuple) or empty list if no result. Automatically add 'limit ?,?' after sql statement if not.
    sql: SELECT * FROM user WHERE name=? and age=?  -->  args: ('张三', 20)
         SELECT * FROM user WHERE name=:name and age=:age   -->  kwargs: ('张三', 20) --> kwargs: {'name': '张三', 'age': 20}
    """
    page_log('select_page', sql, page_num, page_size, *args, **kwargs)
    sql, args = sql_support.dynamic_sql(sql, *args, **kwargs)
    return do_select_page(sql, page_num, page_size, *args)


def do_query_page(sql: str, page_num=1, page_size=10, *args):
    """
    Execute select SQL and return list results(dict).
    sql: SELECT * FROM user WHERE name=? and age=?  -->  args: ('张三', 20)
    """
    do_page_log('select_page', sql.strip(), page_num, page_size, args)
    sql, args = sql_support.page_sql_args(sql, page_num, page_size, *args)
    return query(sql, *args)


def do_select_page(sql: str, page_num=1, page_size=10, *args):
    """
    Execute select SQL and return list results(dict).
    sql: SELECT * FROM user WHERE name=? and age=?  -->  args: ('张三', 20)
    """
    do_page_log('do_select_page', sql.strip(), page_num, page_size, args)
    sql, args = sql_support.page_sql_args(sql, page_num, page_size, *args)
    return select(sql, *args)