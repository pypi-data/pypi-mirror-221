import importlib
from .engine import Engine
from .support import DBError
from .log_support import logger
from .constant import DRIVERS, UNKNOW


def import_driver(driver):
    creator = None
    if driver:
        if driver not in DRIVERS:
            logger.warning(f"Driver '{driver}' not support now, may be you should adapte it youself.")
        engine = DRIVERS.get(driver)
        creator = do_import(driver, engine)
    else:
        curr_engine = Engine.current_engine()
        drivers = dict(filter(lambda x: x[1] == curr_engine, DRIVERS.items())) if curr_engine and curr_engine != UNKNOW else DRIVERS
        for driver, engine in drivers.items():
            try:
                creator = importlib.import_module(driver)
                break
            except ModuleNotFoundError:
                pass
        if not creator:
            raise DBError(f"You may forgot install driver, may be one of {list(DRIVERS.keys())} suit you.")
    return engine, driver, creator


def do_import(driver, Engine):
    try:
        return importlib.import_module(driver)
    except ModuleNotFoundError:
        raise DBError(f"Import {Engine} driver '{driver}' failed, please sure it was installed or change other driver.")
