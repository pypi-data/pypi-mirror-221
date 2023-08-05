import re
from enum import Enum
from typing import Sequence
from .support import DBError
from functools import lru_cache
from .log_support import logger
from .constant import CACHE_SIZE, MYSQL_COLUMN_SQL, POSTGRES_COLUMN_SQL

_ENGIN = None
_DB_ENGIN = None


class Engin(Enum):
    MYSQL = 'MySQL'
    POSTGRESQL = 'PostgreSQL'
    OTHER = 'other'

    @staticmethod
    def current_engin():
        global _ENGIN
        return _ENGIN


class DBEngin:
    before_execute = None
    before_execute = None
    before_execute = None
    before_execute = None
    before_execute = None

    @classmethod
    def init_db_engin(cls, engin, show_sql):
        global _ENGIN
        global _DB_ENGIN
        _ENGIN = engin
        if engin == Engin.MYSQL:
            _DB_ENGIN = MySqlEngin(show_sql)
        elif engin == Engin.POSTGRESQL:
            _DB_ENGIN = PostgresEngin(show_sql)
        elif engin == Engin.OTHER:
            _DB_ENGIN = BaseEngin(show_sql)
        else:
            raise DBError("Unknown engin type: {}".format(engin))

        cls.before_execute = _DB_ENGIN.before_execute
        cls.page_sql_args = _DB_ENGIN.page_sql_args
        cls.create_insert_sql = _DB_ENGIN.create_insert_sql
        cls.get_select_key = _DB_ENGIN.get_select_key
        cls.get_column_sql = _DB_ENGIN.get_column_sql


class BaseEngin:
    def __init__(self, show_sql):
        self.show_sql = show_sql

    def before_execute(self, function: str, sql: str, *args):
        if self.show_sql:
            logger.info("Exec func 'sqlexec.%s' \n\tSQL: %s \n\tARGS: %s" % (function, sql, args))
        if '%' in sql and 'like' in sql.lower():
            sql = sql.replace('%', '%%').replace('%%%%', '%%')
        return sql.replace('?', '%s')

    @staticmethod
    @lru_cache(maxsize=CACHE_SIZE)
    def create_insert_sql(table: str, cols: Sequence[str]):
        columns, placeholders = zip(*[('{}'.format(col), '?') for col in cols])
        return 'INSERT INTO {}({}) VALUES({})'.format(table, ', '.join(columns), ','.join(placeholders))

    @staticmethod
    def page_sql_args(require_limit, sql: str, start, page_size, *args):
        pass

    @staticmethod
    def get_select_key(*args, **kwargs):
        pass

    @staticmethod
    def get_column_sql():
        pass


class MySqlEngin(BaseEngin):

    def __init__(self, show_sql):
        super().__init__(show_sql)

    @staticmethod
    def page_sql_args(require_limit, sql: str, start, page_size, *args):
        if require_limit(sql):
            sql = '{} limit ?, ?'.format(sql)
        args = [*args, start, page_size]
        return sql, args

    @staticmethod
    def get_select_key(*args, **kwargs):
        return "SELECT LAST_INSERT_ID()"

    @staticmethod
    def get_column_sql():
        return MYSQL_COLUMN_SQL


class PostgresEngin(BaseEngin):

    def __init__(self, show_sql):
        super().__init__(show_sql)


    @staticmethod
    def page_sql_args(require_limit, sql: str, start, page_size, *args):
        if require_limit(sql):
            sql = '{} LIMIT ? OFFSET ?'.format(sql)
        args = [*args, page_size, start]
        return sql, args

    @staticmethod
    def get_select_key(key_seq: str = None, table: str = None, sql: str = None):
        if not key_seq:
            if table:
                key_seq = PostgresEngin._build_key_seq(table)
            else:
                if sql:
                    key_seq = PostgresEngin._get_key_seq_from_sql(sql)
                else:
                    raise DBError("Get PostgreSQL select key fail, all of 'key_seq', 'table', 'sql' are None")
        return f"SELECT currval('{key_seq}')"

    @staticmethod
    def get_column_sql():
        return POSTGRES_COLUMN_SQL

    @staticmethod
    def _build_key_seq(table: str):
        return f'{table}_id_seq'

    @staticmethod
    @lru_cache(maxsize=CACHE_SIZE)
    def _get_key_seq_from_sql(sql: str):
        table = re.search('(?<=into )\w+', sql, re.I)
        key_seq = PostgresEngin._build_key_seq(table.group())
        logger.warning("'key_seq' is None, will use default '{}' from sql.".format(key_seq))
        return key_seq
