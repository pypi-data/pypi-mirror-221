from . import PostgresEngin
from .log_support import sql_id_log
from sqlbatis import sql_holder as holder
from sqlbatis.dbx import insert, save_sql, batch_insert, batch_execute, execute, get, query, query_one, select, select_one, query_page, select_page


def save(sql_id: str, *args, **kwargs):
    """
    Execute insert SQL, return primary key.
    :return: Primary key
    """
    sql_id_log('dbx.save', sql_id, *args, **kwargs)
    sql_model = holder.get_sql_model(sql_id)
    sql, args = holder.do_get_sql(sql_model, False, None, *args, **kwargs)
    select_key = PostgresEngin.get_select_key(key_seq=sql_model.key_seq, sql=sql)
    return save_sql(select_key, sql, *args)
