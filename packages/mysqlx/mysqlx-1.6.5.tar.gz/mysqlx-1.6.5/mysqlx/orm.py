import sys
from . import get_snowflake_id
from .db import insert, do_execute, save, do_query_page, do_select_page
from .log_support import orm_insert_log, logger, orm_page_log, orm_by_page_log
from sqlbatis.constant import LIMIT_1, NO_LIMIT
from typing import Union, Sequence
from datetime import datetime
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
            return save(table, **kwargs)

    @classmethod
    def update_by_id(cls, _id: Union[int, str], **kwargs):
        """
        rowcount = User.update_by_id(id=1, name='王五')
        return: Effect rowcount
        """
        logger.debug("Exec func 'mysqlx.orm.Model.%s' \n\t Class: '%s', id: %d, kwargs: %s" % ('update_by_id', cls.__name__, _id, kwargs))
        assert kwargs, 'Must set update kv'
        key = cls._get_key()
        where = '`%s` = ?' % key
        cols, args = zip(*kwargs.items())
        sql, update_time_arg = cls._update_sql(where, *cols)
        if update_time_arg:
            args = [*args, update_time_arg]
        return do_execute(sql, *args, _id, LIMIT_1)

    @classmethod
    def delete_by_id(cls, _id: Union[int, str]):
        """
        Physical delete
        rowcount = User.delete_by_id(id=1)
        return: Effect rowcount
        """
        logger.debug("Exec func 'mysqlx.orm.Model.%s' \n\t Class: '%s', id: %d" % ('delete_by_id', cls.__name__, _id))
        key, table = cls._get_key_and_table()
        sql = 'DELETE FROM `%s` WHERE `%s` = ? LIMIT ?' % (table, key)
        return do_execute(sql, _id, LIMIT_1)

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
    def _update_sql(cls, where, *update_fields):
        update_time_arg = None
        table = cls._get_table()
        update_time_field = cls._get_update_time_field()
        if update_time_field is not None and update_time_field not in update_fields:
            update_fields = [*update_fields, update_time_field]
            update_time_arg = datetime.now()

        update_fields = ','.join(['`{}` = ?'.format(col) for col in update_fields])
        return 'UPDATE `{}` SET {} WHERE {} LIMIT ?'.format(table, update_fields, where), update_time_arg

    @classmethod
    def _logical_delete_by_id_op(cls, _id: Union[int, str], update_by: Union[int, str] = None, del_status=DelFlag.DELETED):
        key, table = cls._get_key_and_table()
        del_flag_field = cls._get_del_flag_field()
        update_by_field = cls._get_update_by_field()

        where = '`%s` = ?' % key
        if update_by is not None and update_by_field is not None:
            sql, update_time_arg = cls._update_sql(where, del_flag_field, update_by_field)
            if update_time_arg:
                return do_execute(sql, del_status.value, update_by, update_time_arg, _id, LIMIT_1)
            return do_execute(sql, del_status.value, update_by, _id, LIMIT_1)
        else:
            sql, update_time_arg = cls._update_sql(where, del_flag_field)
            if update_time_arg:
                return do_execute(sql, del_status.value, update_time_arg, _id, LIMIT_1)
            return do_execute(sql, del_status.value, _id, LIMIT_1)

    @classmethod
    def _do_logical_delete_by_ids(cls, ids: Union[Sequence[int], Sequence[str]], update_by: Union[int, str] = None, del_status=DelFlag.DELETED):
        ids_size = len(ids)
        key = cls._get_key()
        del_flag_field = cls._get_del_flag_field()
        update_by_field = cls._get_update_by_field()

        where = '`%s` in (%s)' % (key, ','.join(['?' for _ in range(ids_size)]))
        if update_by is not None and update_by_field is not None:
            sql, update_time_arg = cls._update_sql(where, del_flag_field, update_by_field)
            if update_time_arg:
                return do_execute(sql, del_status.value, update_by, update_time_arg, *ids, ids_size)
            return do_execute(sql, del_status.value, update_by, *ids, ids_size)
        else:
            sql, update_time_arg = cls._update_sql(where, del_flag_field)
            if update_time_arg:
                return do_execute(sql, del_status.value, update_time_arg, *ids, ids_size)
            return do_execute(sql, del_status.value, *ids, ids_size)

    @classmethod
    def _delete_by_ids(cls, ids: Union[Sequence[int], Sequence[str]]):
        ids_size = len(ids)
        key, table = cls._get_key_and_table()
        sql = 'DELETE FROM `{}` WHERE `{}` in ({}) LIMIT ?'.format(table, key, ','.join(['?' for _ in range(ids_size)]))
        return do_execute(sql, *ids, ids_size)

