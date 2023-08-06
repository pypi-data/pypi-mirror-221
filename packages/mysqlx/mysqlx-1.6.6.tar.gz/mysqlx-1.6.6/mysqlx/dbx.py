from .engin import MySqlEngin
from .log_support import sql_id_log
from sqlbatis import sql_holder as holder
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
