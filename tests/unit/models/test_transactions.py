from unittest import TestCase, mock

from pymongo.errors import BulkWriteError

from app.models.transactions import Transactions
from app.utils.responses.structures.internal_process import InternalProcess


class TestTransactions(TestCase):

    @mock.patch('app.models.transactions.BaseLogger')
    @mock.patch('app.models.transactions.mongo_db.cx')
    def setUp(self, mock_cx, mock_logger) -> None:
        self.trans = Transactions()

    def test_execute_transaction(self):
        collection = mock.Mock()
        bulk_api = mock.Mock()
        output = self.trans.execute_transaction(collection, bulk_api)
        self.assertIsInstance(output, InternalProcess)

    def test_execute_transaction_failure(self):
        collection = mock.Mock()
        bulk_api = mock.Mock()
        collection.bulk_write.side_effect = BulkWriteError({'error': 'Error Dummy'})
        output = self.trans.execute_transaction(collection, bulk_api)
        self.assertIsInstance(output, InternalProcess)
        self.assertFalse(output.operation)

