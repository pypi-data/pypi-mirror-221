# Don't remove. Import for not repetitive implementation
from sqlbatis.log_support import logger, sql_id_log


def save_log(table, **kwargs):
    logger.debug("Exec func 'mysqlx.db.save' \n\t Table: '%s', kwargs: %s" % (table, kwargs))


def orm_insert_log(function, class_name, **kwargs):
    logger.debug("Exec func 'mysqlx.orm.Model.%s' \n\t Class: '%s', kwargs: %s" % (function, class_name, kwargs))
