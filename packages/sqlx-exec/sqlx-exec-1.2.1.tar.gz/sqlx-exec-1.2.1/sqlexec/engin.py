from typing import Sequence
from functools import lru_cache
from .constant import CACHE_SIZE, UNKNOW

_ENGIN = None


class Engin:
    def __init__(self, name=UNKNOW):
        self.name = name

    @classmethod
    def init(cls, name=UNKNOW):
        global _ENGIN
        if _ENGIN:
            if _ENGIN.name == UNKNOW and name != UNKNOW:
                _ENGIN.name = name
        else:
            _ENGIN = cls(name)

    @staticmethod
    def current_engin():
        global _ENGIN
        if _ENGIN:
            return _ENGIN.name
        return None

    @classmethod
    @lru_cache(maxsize=CACHE_SIZE)
    def create_insert_sql_intf(cls, table: str, cols: Sequence[str]):
        return _ENGIN.create_insert_sql(table, cols)

    @staticmethod
    def create_insert_sql(table: str, cols: Sequence[str]):
        columns, placeholders = zip(*[('{}'.format(col), '?') for col in cols])
        return 'INSERT INTO {}({}) VALUES({})'.format(table, ', '.join(columns), ','.join(placeholders))
