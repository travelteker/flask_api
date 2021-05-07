from os import environ
from unittest import TestCase, mock

from app.utils.conditions.operation_mode import OperationMode


class TestOperationMode(TestCase):

    @mock.patch('app.utils.conditions.operation_mode.exit')
    @mock.patch.dict(environ, {'ENV': 'a'})
    @mock.patch.dict(environ, {'WHITE_LIST_MODE': 'aaa, bbb'})
    def test_trigger_action(self, mock_exit):
        OperationMode.trigger_action()
        self.assertTrue(mock_exit.called)

