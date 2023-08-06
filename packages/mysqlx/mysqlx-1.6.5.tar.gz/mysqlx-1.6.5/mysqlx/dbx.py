from .engin import MySqlEngin
from sqlbatis import sql_holder as holder
from .db import do_query_page, do_select_page
from .log_support import page_sql_id_log, sql_id_log
from sqlbatis.dbx import insert, save_sql, batch_insert, batch_execute, execute, get, query, query_one, select, select_one


def save(sql_id: str, *args, **kwargs):
    """
    Execute insert SQL, return primary key.
    :return: Primary key
    """
    sql_id_log('dbx.save', sql_id, *args, **kwargs)
    sql, args = holder.get_sql(sql_id, *args, **kwargs)
    select_key = MySqlEngin.get_select_key()
    return save_sql(select_key, sql, *args)


def query_page(sql_id: str, page_num=1, page_size=10, *args, **kwargs):
    """
    Execute select SQL and return list or empty list if no result. Automatically add 'limit ?,?' after sql statement if not.
    sql: SELECT * FROM person WHERE name=? and age=?  -->  args: ('张三', 20)
         SELECT * FROM person WHERE name=:name and age=:age  -->  kwargs: ('张三', 20) --> kwargs: {'name': '张三', 'age': 20}
    """
    page_sql_id_log('query_page', sql_id, page_num, page_size, *args, **kwargs)
    sql, args = holder.get_sql(sql_id, *args, **kwargs)
    return do_query_page(sql, page_num, page_size, *args)


def select_page(sql_id: str, page_num=1, page_size=10, *args, **kwargs):
    """
    Execute select SQL and return list or empty list if no result. Automatically add 'limit ?,?' after sql statement if not.
    sql: SELECT * FROM person WHERE name=? and age=?  -->  args: ('张三', 20)
         SELECT * FROM person WHERE name=:name and age=:age  -->  kwargs: ('张三', 20) --> kwargs: {'name': '张三', 'age': 20}
    """
    page_sql_id_log('select_page', sql_id, page_num, page_size, *args, **kwargs)
    sql, args = holder.get_sql(sql_id, *args, **kwargs)
    return do_select_page(sql, page_num, page_size, *args)