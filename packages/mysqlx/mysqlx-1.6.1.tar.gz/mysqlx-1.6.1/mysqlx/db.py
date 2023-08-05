from .log_support import save_log
from sqlbatis import Engin, DBEngin

# Don't remove. Import for not repetitive implementation
from sqlbatis.db import init_db as supper_init_db, insert, save as save_select_key, execute, batch_insert, batch_execute, get, query, query_one, \
    query_page, select, select_one, select_page, do_execute, do_get, do_query, do_query_one, do_query_page, do_select, do_select_one, do_select_page

_DB_CTX = None


def init_db(user='root', password='', database='test', host='127.0.0.1', port=3306, pool_size=0, show_sql=False, use_unicode=True, **kwargs):
    supper_init_db(user=user, password=password, database=database, host=host, port=port, engin=Engin.MYSQL, pool_size=pool_size, show_sql=show_sql, \
                   use_unicode=use_unicode, **kwargs)


def save(table: str, **kwargs):
    """
    Insert data into table, return primary key.
    :param table: table
    :param kwargs:
    :return: Primary key
    """
    save_log(table, **kwargs)
    return save_select_key(DBEngin.get_select_key(), table, **kwargs)


