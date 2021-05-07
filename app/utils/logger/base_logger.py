import logging
from logging import DEBUG, Formatter
from logging.handlers import TimedRotatingFileHandler
from os import sep, getcwd, getenv


class BaseLogger:

    """Logger to register information in distinct files"""

    LOG_DEFAULT = 'plytix.log'
    FORMAT_DEFAULT = '%(asctime)s|%(name)s|%(threadName)s|%(levelname)s|%(message)s'

    def __init__(self, formatter: str = None, level: int = None):
        self.__formatter = formatter or type(self).FORMAT_DEFAULT
        self.__level = level or DEBUG
        self.__module = type(self).__module__

    def create_logger(self, title: str, name_file: str = None):
        name_file = name_file or type(self).LOG_DEFAULT
        logger = logging.getLogger(title)
        logger.propagate = False
        logger.setLevel(self.__level)
        full_name = sep.join([getcwd(), getenv('DIR_LOGS'), name_file])
        if not logger.handlers:
            handler = TimedRotatingFileHandler(filename=full_name, when="h", interval=12, backupCount=5)
            logger_formatter = Formatter(self.__formatter)
            handler.setFormatter(logger_formatter)
            logger.addHandler(handler)
        return logger
