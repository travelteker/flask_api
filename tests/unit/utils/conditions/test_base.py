from os import environ
from unittest import TestCase, mock

from app.utils.conditions.base import Base


class TestBase(TestCase):

    def setUp(self) -> None:
        self.base = Base()

    @mock.patch('app.utils.conditions.base.CreateDir.trigger_action')
    @mock.patch('app.utils.conditions.base.Version.trigger_action')
    @mock.patch('app.utils.conditions.base.OperationMode.trigger_action')
    def test_apply_conditions(self, mock_mode, mock_version, mock_create):
        self.base.apply_conditions()
        self.assertTrue(mock_mode.called)
        self.assertTrue(mock_version.called)
        self.assertTrue(mock_create.called)


