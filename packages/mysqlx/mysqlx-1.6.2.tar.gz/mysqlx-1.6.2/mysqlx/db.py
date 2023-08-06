from .log_support import save_log
from sqlexec.engin import MySqlEngin

# Don't remove. Import for not repetitive implementation
from sqlbatis.db import insert, save as save_select_key, execute, batch_insert, batch_execute, get, query, query_one, query_page, select, select_one,\
    select_page, do_execute, do_get, do_query, do_query_one, do_query_page, do_select, do_select_one, do_select_page


def save(table: str, **kwargs):
    """
    Insert data into table, return primary key.
    :param table: table
    :param kwargs:
    :return: Primary key
    """
    save_log(table, **kwargs)
    return save_select_key(MySqlEngin.get_select_key(), table, **kwargs)


