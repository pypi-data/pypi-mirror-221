from typing import Sequence
from functools import lru_cache
from .constant import CACHE_SIZE

_ENGIN = None


class Engin:
    def __init__(self, name=None):
        self.name = name

    @classmethod
    def init(cls, name=None):
        global _ENGIN
        if _ENGIN:
            if name and not _ENGIN.name:
                _ENGIN.name = name
        else:
            _ENGIN = cls(name)

    @staticmethod
    def current_engin():
        global _ENGIN
        return _ENGIN.name

    @classmethod
    @lru_cache(maxsize=CACHE_SIZE)
    def create_insert_sql(cls, table: str, cols: Sequence[str]):
        return _ENGIN._create_insert_sql(table, cols)

    @staticmethod
    def page_sql_args(require_limit, sql: str, start: int, page_size: int, *args):
        return _ENGIN._page_sql_args(require_limit, sql, start, page_size, *args)

    @staticmethod
    def get_select_key(*args, **kwargs):
        return _ENGIN._get_select_key(*args, **kwargs)

    @staticmethod
    @lru_cache(maxsize=CACHE_SIZE)
    def get_table_columns(table: str):
        return _ENGIN._get_table_columns(table)

    @staticmethod
    def _create_insert_sql(table: str, cols: Sequence[str]):
        columns, placeholders = zip(*[('{}'.format(col), '?') for col in cols])
        return 'INSERT INTO {}({}) VALUES({})'.format(table, ', '.join(columns), ','.join(placeholders))
