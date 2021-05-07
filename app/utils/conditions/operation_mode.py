from os import getenv
from sys import exit


class OperationMode:

    @staticmethod
    def trigger_action():
        """Method to validate exits value MODE_DEFAULT before start application Flask
        :return: None
        """
        mode = getenv('ENV')
        if mode not in getenv("WHITE_LIST_MODE").split(','):
            exit('Aborting execution, please contact with support showing this code <0x00001>')
