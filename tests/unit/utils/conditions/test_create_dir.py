from os import environ
from unittest import TestCase, mock

from app.utils.conditions.create_dir import CreateDir


class TestCreateDir(TestCase):

    @mock.patch('app.utils.conditions.create_dir.mkdir')
    @mock.patch('app.utils.conditions.create_dir.isdir')
    @mock.patch.dict(environ, {'DIR_LOGS': 'logs'})
    def test_trigger_action(self, mock_isdir, mock_mkdir):
        mock_isdir.return_value = False
        CreateDir.trigger_action()
        self.assertTrue(mock_mkdir.called)
