from .snowflake import get_id
from .db import insert, save_key_seq
from .log_support import orm_insert_log

# Don't remove. Import for not repetitive implementation
from sqlbatis.orm import DelFlag, KeyStrategy, Model as BaseModel


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
        db.init_db(person='xxx', password='xxx', database='xxx', host='xxx', ...)  # or dbx.init_db(...) init db first,
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
        key_strategy = cls._get_key_strategy()
        if key_strategy == KeyStrategy.SNOWFLAKE:
            if key in kwargs:
                _id = kwargs[key]
            else:
                _id = get_id()
                kwargs[key] = _id
            insert(table, **kwargs)
        else:
            key_seq = cls._get_key_seq()
            _id = save_key_seq(key_seq, table, **kwargs)
        return _id

   
