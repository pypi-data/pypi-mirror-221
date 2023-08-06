from typing import Sequence
from sqlbatis.engin import Engin, DBError


class MySqlEngin(Engin):
    def __init__(self, engin):
        super().__init__(engin)

    @classmethod
    def init(cls, name='MySQL'):
        super().init(name)

    @staticmethod
    def _create_insert_sql(table: str, cols: Sequence[str]):
        columns, placeholders = zip(*[('`{}`'.format(col), '?') for col in cols])
        return 'INSERT INTO `{}`({}) VALUES({})'.format(table, ','.join(columns), ','.join(placeholders))

    @staticmethod
    def _page_sql_args(require_limit, sql: str, start, page_size, *args):
        if require_limit(sql):
            sql = '{} LIMIT ?, ?'.format(sql)
        args = [*args, start, page_size]
        return sql, args