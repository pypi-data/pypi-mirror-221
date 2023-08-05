from sqlbatis import Engin

# Don't remove. Import for not repetitive implementation
from sqlbatis.dbx import init_db as supper_init_db, insert, batch_insert, save, execute, batch_execute, get, query, query_one, query_page, select, \
    select_one, select_page

def init_db(user='root', password='', database='test', host='127.0.0.1', port=3306, pool_size=0, show_sql=False, mapper_path='mapper', **kwargs):
    supper_init_db(user=user, password=password, database=database, host=host, port=port, mapper_path=mapper_path, engin=Engin.POSTGRESQL, \
                   pool_size=pool_size, show_sql=show_sql, **kwargs)

