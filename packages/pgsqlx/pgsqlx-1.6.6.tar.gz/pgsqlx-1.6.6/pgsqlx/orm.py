import sys
from . import get_snowflake_id
from .db import insert, save_key_seq, do_query_page, do_select_page
from .log_support import orm_insert_log, logger, orm_page_log, orm_by_page_log
from .constant import KEY_SEQ, NO_LIMIT
from sqlbatis.sql_support import simple_sql

# Don't remove. Import for not repetitive implementation
from sqlbatis.orm import DelFlag, KeyStrategy, Model as BaseModel, get_where_arg_limit, select_sql


class Model(BaseModel):
    """
    Create a class extends Model:

    class Person(Model):
        __key__ = 'id'
        __table__ = 'person'
        __update_by__ = 'update_by'
        __update_time__ = 'update_time'
        __del_flag__ = 'del_flag'
        __key_seq__ = 'person_id_seq'

        def __init__(self, id: int = None, name: str = None, age: int = None, update_by: int = None, update_time: datetime = None, del_flag: int = None):
            self.id = id

            self.update_by = update_by
            self.update_time = update_time
            self.del_flag = del_flag
            self.name = name
            self.age = age

    then you can use like follow:
        init_db(person='xxx', password='xxx', database='xxx', host='xxx', ...)  # or dbx.init_db(...) init db first,
        person = Person(name='张三', age=55)
        effect_rowcount = person.persist()
        id = person.inst_save()
    """

    @classmethod
    def save(cls, **kwargs):
        """
        id = Person.save(name='张三', age=20)
        :return: Primary key
        """
        orm_insert_log('save', cls.__name__, **kwargs)
        key, table = cls._get_key_and_table()
        if key in kwargs:
            insert(table, **kwargs)
            return kwargs[key]

        key_strategy = cls._get_key_strategy()
        if key_strategy == KeyStrategy.SNOWFLAKE:
            kwargs[key] = get_snowflake_id()
            insert(table, **kwargs)
            return kwargs[key]
        else:
            key_seq = cls._get_key_seq()
            return save_key_seq(key_seq, table, **kwargs)

    @classmethod
    def find_page(cls, page_num=1, page_size=10, *fields, **kwargs):
        """
        Return list(object) or empty list if no result.
        persons = Person.find_page(1, 10, 'name', 'age', name='张三', age=55)
        :param page_num: page number
        :param page_size: page size
        :param fields: Default select all fields if not set
        """
        orm_page_log('find_page', page_num, page_size, cls.__name__, *fields, **kwargs)
        result = cls.query_page(page_num, page_size, *fields, **kwargs)
        return [cls.to_obj(**d) for d in result]

    @classmethod
    def find_page_by(cls, page_num: int, page_size: int, where: str, *args, **kwargs):
        """
        Return list(dict) or empty list if no result. Automatically add 'limit ?,?' after where if not.
        rows = Person.find_by_page(1, 10, 'where name=?', '李四')
        """
        orm_page_log(sys._getframe().f_code.co_name, page_num, page_size, cls.__name__, where, *args, **kwargs)
        return [cls.to_obj(**d) for d in cls.query_page_by(page_num, page_size, where, *args, **kwargs)]

    @classmethod
    def query_page(cls, page_num=1, page_size=10, *fields, **kwargs):
        """
        Return list(dict) or empty list if no result.
        persons = Person.query_page(1, 10, 'id', 'name', 'age', name='张三', age=55)
        :param page_num: page number
        :param page_size: page size
        :param fields: Default select all fields if not set
        """
        orm_page_log('query_page', page_num, page_size, cls.__name__, *fields, **kwargs)
        table = cls._get_table()
        where, args, _ = get_where_arg_limit(**kwargs)
        sql = select_sql(table, where, NO_LIMIT, *fields)
        return do_query_page(sql, page_num, page_size, *args)

    @classmethod
    def query_page_by(cls, page_num: int, page_size: int, where: str, *args, **kwargs):
        """
        Return list(dict) or empty list if no result. Automatically add 'limit ?,?' after where if not.
        rows = Person.query_by_page(1, 10, 'where name=?', '李四')
        """
        orm_by_page_log(sys._getframe().f_code.co_name, page_num, page_size, cls.__name__, where, *args, **kwargs)
        sql = cls._where_sql(where)
        sql, args = simple_sql(sql, *args, **kwargs)
        return do_query_page(sql, page_num, page_size, *args)

    @classmethod
    def select_page(cls, page_num=1, page_size=10, *fields, **kwargs):
        """
        Return list(dict) or empty list if no result.
        rows = Person.select_page('id', 'name', 'age', name='张三', age=55)
        :param page_num: page number
        :param page_size: page size
        :param fields: Default select all fields if not set
        """
        orm_page_log('select_page', page_num, page_size, cls.__name__, *fields, **kwargs)
        table = cls._get_table()
        where, args, _ = get_where_arg_limit(**kwargs)
        sql = select_sql(table, where, NO_LIMIT, *fields)
        return do_select_page(sql, page_num, page_size, *args)

    @classmethod
    def select_page_by(cls, page_num: int, page_size: int, where: str, *args, **kwargs):
        """
        Return list(dict) or empty list if no result. Automatically add 'limit ?,?' after where if not.
        rows = Person.select_by_page(1, 10, 'where name=?', '李四')
        """
        orm_by_page_log(sys._getframe().f_code.co_name, page_num, page_size, cls.__name__, where, *args, **kwargs)
        sql = cls._where_sql(where)
        sql, args = simple_sql(sql, *args, **kwargs)
        return do_select_page(sql, page_num, page_size, *args)


    @classmethod
    def _get_key_seq(cls):
        if hasattr(cls, KEY_SEQ):
            return cls.__key_seq__
        logger.warning("%s not set attribute '%s'" % (cls.__name__, KEY_SEQ))
        pk, table = cls._get_pk_and_table()
        return "{}_{}_seq".format(table, pk)

   
