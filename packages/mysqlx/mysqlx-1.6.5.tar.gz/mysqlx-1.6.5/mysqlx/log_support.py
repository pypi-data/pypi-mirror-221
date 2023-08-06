from sqlbatis.log_support import logger, sql_id_log


def save_log(table, **kwargs):
    logger.debug("Exec func 'mysqlx.db.save' \n\t Table: '%s', kwargs: %s" % (table, kwargs))


def orm_insert_log(function, class_name, **kwargs):
    logger.debug("Exec func 'mysqlx.orm.Model.%s' \n\t Class: '%s', kwargs: %s" % (function, class_name, kwargs))


def do_page_log(function: str, sql: str, page_num, page_size, *args):
    logger.debug(
        "Exec func 'mysqlx.db.%s', page_num: %d, page_size: %d \n\t sql: %s \n\t args: %s" % (function, page_num, page_size, sql.strip(), args))


def page_log(function: str, sql: str, page_num, page_size, *args, **kwargs):
    logger.debug("Exec func 'mysqlx.db.%s', page_num: %d, page_size: %d \n\tsql: %s \n\targs: %s \n\tkwargs: %s" % (
        function, page_num, page_size, sql.strip(), args, kwargs))


def page_sql_id_log(function: str, sql_id: str, page_num, page_size, *args, **kwargs):
    logger.debug("Exec func 'mysqlx.%s', page_num: %d, page_size: %d, sql_id: %s, args: %s, kwargs: %s" % (function, page_num, page_size, sql_id, args, kwargs))


def orm_page_log(function, page_num, page_size, class_name, *fields, **kwargs):
    logger.debug("Exec func 'mysqlx.orm.Model.%s', page_num: %d, page_size: %d \n\t Class: '%s', fields: %s, kwargs: %s" % (
        function, page_num, page_size, class_name, fields, kwargs))


def orm_by_page_log(function, page_num, page_size, class_name, where, *args, **kwargs):
    logger.debug("Exec func 'sqlx-batis.orm.Model.%s', page_num: %d, page_size: %d \n\t Class: '%s', where: %s, args: %s, kwargs: %s" % (
        function, page_num, page_size, class_name, where, args, kwargs))
