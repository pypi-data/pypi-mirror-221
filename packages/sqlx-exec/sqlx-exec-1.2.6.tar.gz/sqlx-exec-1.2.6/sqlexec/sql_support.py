import re
from .engine import Engine
from typing import Sequence
from functools import lru_cache
from .constant import CACHE_SIZE, NAMED_REGEX

def insert_sql_args(table: str, **kwargs):
    cols, args = zip(*kwargs.items())
    sql = Engine.create_insert_sql_intf(table, cols)
    return sql, args


def get_batch_args(*args):
    return args[0] if isinstance(args, tuple) and len(args) == 1 and isinstance(args[0], Sequence) else args


def batch_insert_sql_args(table: str, *args):
    args = get_batch_args(*args)
    args = [zip(*arg.items()) for arg in args]  # [(cols, args)]
    cols, args = zip(*args)  # (cols), (args)
    sql = Engine.create_insert_sql_intf(table, cols[0])
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
