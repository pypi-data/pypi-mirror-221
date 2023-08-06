import importlib
from .engin import Engin
from .support import DBError
from .log_support import logger
from .constant import DRIVERS, UNKNOW


def import_driver(driver):
    creator = None
    if driver:
        if driver not in DRIVERS:
            logger.warning(f"Driver '{driver}' not support now, may be you should adapte it youself.")
        engin = DRIVERS.get(driver)
        creator = do_import(driver, engin)
    else:
        curr_engin = Engin.current_engin()
        drivers = dict(filter(lambda x: x[1] == curr_engin, DRIVERS.items())) if curr_engin and curr_engin != UNKNOW else DRIVERS
        for driver, engin in drivers.items():
            try:
                creator = importlib.import_module(driver)
                break
            except ModuleNotFoundError:
                pass
        if not creator:
            raise DBError(f"You may forgot install driver, may be one of {list(DRIVERS.keys())} suit you.")
    return engin, driver, creator


def do_import(driver, engin):
    try:
        return importlib.import_module(driver)
    except ModuleNotFoundError:
        raise DBError(f"Import {engin} driver '{driver}' failed, please sure it was installed or change other driver.")
