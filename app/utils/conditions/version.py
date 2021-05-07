from os import getenv
from sys import version_info, exit


class Version:

    @staticmethod
    def trigger_action():
        """Method to validate minimal version Python before execute application Flask
        :return: None
        """
        major, minor, micro, *others = version_info
        version_detected = f'{major}{minor}{micro}'
        version_minimal = getenv('MINIMAL_VERSION')
        if version_detected < version_minimal:
            exit('Aborting execution, please contact with support showing this code <0x00002>')

