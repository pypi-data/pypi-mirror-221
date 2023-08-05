import re
from typing import Sequence
from functools import lru_cache
from .engin import DBEngin
from .constant import CACHE_SIZE, NAMED_REGEX


def insert_sql_args(table: str, **kwargs):
    cols, args = zip(*kwargs.items())
    sql = DBEngin.create_insert_sql(table, cols)
    return sql, args


def get_batch_args(*args):
    return args[0] if isinstance(args, tuple) and len(args) == 1 and isinstance(args[0], Sequence) else args


def batch_insert_sql_args(table: str, *args):
    args = get_batch_args(*args)
    args = [zip(*arg.items()) for arg in args]  # [(cols, args)]
    cols, args = zip(*args)  # (cols), (args)
    sql = DBEngin.create_insert_sql(table, cols[0])
    return sql, args


def batch_named_sql_args(sql: str, *args):
    args = get_batch_args(*args)
    args = [get_named_args(sql, **arg) for arg in args]
    sql = get_named_sql(sql)
    return sql, args


@lru_cache(maxsize=CACHE_SIZE)
def get_named_sql(sql: str):
    return re.sub(NAMED_REGEX, '?', sql)


def get_named_args(sql: str, **kwargs):
    return [kwargs[r[1:]] for r in re.findall(NAMED_REGEX, sql)]


def page_sql_args(sql: str, page_num=1, page_size=10, *args):
    start = (page_num - 1) * page_size
    return DBEngin.page_sql_args(require_limit, sql, start, page_size, *args)


def require_limit(sql: str):
    lower_sql = sql.lower()
    if 'limit' not in lower_sql:
        return True
    idx = lower_sql.rindex('limit')
    if idx > 0 and ')' in lower_sql[idx:]:
        return True
    return False
