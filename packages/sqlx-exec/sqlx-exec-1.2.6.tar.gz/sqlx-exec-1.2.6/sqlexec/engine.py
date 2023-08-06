from typing import Sequence
from functools import lru_cache
from .constant import CACHE_SIZE, UNKNOW

_ENGINE = None


class Engine:
    def __init__(self, name=UNKNOW):
        self.name = name

    @classmethod
    def init(cls, name=UNKNOW):
        global _ENGINE
        if _ENGINE:
            if _ENGINE.name == UNKNOW and name != UNKNOW:
                _ENGINE.name = name
        else:
            _ENGINE = cls(name)

    @staticmethod
    def current_engine():
        global _ENGINE
        if _ENGINE:
            return _ENGINE.name
        return None

    @classmethod
    @lru_cache(maxsize=CACHE_SIZE)
    def create_insert_sql_intf(cls, table: str, cols: Sequence[str]):
        return _ENGINE.create_insert_sql(table, cols)

    @staticmethod
    def get_page_sql_args_intf(sql: str, page_num: int, page_size: int, *args):
        return _ENGINE.get_page_sql_args(sql, page_num, page_size, *args)

    @staticmethod
    def get_select_key_intf(*args, **kwargs):
        return _ENGINE.get_select_key(*args, **kwargs)

    @staticmethod
    def get_table_columns_intf(table: str):
        return _ENGINE.get_table_columns(table)

    @staticmethod
    def create_insert_sql(table: str, cols: Sequence[str]):
        columns, placeholders = zip(*[('{}'.format(col), '?') for col in cols])
        return 'INSERT INTO {}({}) VALUES({})'.format(table, ', '.join(columns), ','.join(placeholders))
