from typing import Any, List

from pymongo.errors import BulkWriteError

from app.models import mongo_db
from app.utils.logger.base_logger import BaseLogger
from app.utils.responses.structures.internal_process import InternalProcess


class Transactions:

    """Class to manage transactions"""

    def __init__(self):
        self.__module = type(self).__name__
        self.client = mongo_db.cx
        self.__logger = BaseLogger().create_logger(self.__module, 'transactions.log')

    def execute_transaction(self, collection: Any, bulk_api: List[Any]) -> InternalProcess:
        action = True
        message = 'Operation <execute_transaction()> successfully'
        with self.client.start_session() as session:
            with session.start_transaction():
                try:
                    collection.bulk_write(bulk_api)
                except BulkWriteError as err:
                    message = f'{self.__module}|____execute_transaction()|description:{err.details}'
                    self.__logger.critical(message)
                    action = False
        return InternalProcess(action, message)

