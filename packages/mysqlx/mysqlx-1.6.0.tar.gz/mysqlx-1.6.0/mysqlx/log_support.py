from sqlbatis.log_support import logger


def save_log(table, **kwargs):
    logger.debug("Exec func 'pgsqlx.db.save' \n\t Table: '%s', kwargs: %s" % (table, kwargs))


def orm_insert_log(function, class_name, **kwargs):
    logger.debug("Exec func 'mysqlx.orm.Model.%s' \n\t Class: '%s', kwargs: %s" % (function, class_name, kwargs))
