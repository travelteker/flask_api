from os import getenv, sep, getcwd, mkdir
from os.path import isdir


class CreateDir:

    @staticmethod
    def trigger_action():
        """Method to create logs dir if not exists"""
        dir_logs = getenv('DIR_LOGS')
        path_logs = sep.join([getcwd(), dir_logs])
        if not isdir(path_logs):
            mkdir(path_logs)
