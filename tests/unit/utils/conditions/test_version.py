from os import environ
from unittest import TestCase, mock

from app.utils.conditions.version import Version


class TestVersion(TestCase):

    @mock.patch('app.utils.conditions.version.exit')
    @mock.patch.dict(environ, {'MINIMAL_VERSION': '999'})
    def test_trigger_action(self, mock_exit):
        Version.trigger_action()
        self.assertTrue(mock_exit.called)

