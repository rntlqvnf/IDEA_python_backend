import logging

def __get_logger():
    __logger = logging.getLogger('logger')
    formatter = logging.Formatter(
        '%(levelname)s##%(asctime)s##%(message)s')
    fileHandler = logging.FileHandler('./logs/log.txt')
    fileHandler.setFormatter(formatter)
    __logger.addHandler(fileHandler)
    __logger.setLevel(logging.DEBUG)

    return __logger

logger = __get_logger()