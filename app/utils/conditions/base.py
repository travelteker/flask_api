from app.utils.conditions import OperationMode, Version, CreateDir


class Base:

    """Class to apply conditions before to start the application"""

    CONDITIONS = [OperationMode, Version, CreateDir]

    def __init__(self):
        self.__module = type(self).__name__

    def apply_conditions(self):
        for condition in type(self).CONDITIONS:
            condition.trigger_action()
