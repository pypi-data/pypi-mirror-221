from .support import DB_LOCK

MAX_POOL_SIZE = 32
_CONNECTION_POOL = None

def pooled_connect(creator, pool_size, **kwargs):
    global _CONNECTION_POOL
    assert 1 <= pool_size <= MAX_POOL_SIZE, 'pool_size should be higher or equal to 1 and lower or equal to {}'.format(MAX_POOL_SIZE)
    if _CONNECTION_POOL is None:
        with DB_LOCK:
            if _CONNECTION_POOL is None:
                from dbutils.pooled_db import PooledDB
                _CONNECTION_POOL = PooledDB(creator, mincached=pool_size, maxcached=pool_size, maxconnections=MAX_POOL_SIZE, **kwargs)

    return _CONNECTION_POOL.connection

