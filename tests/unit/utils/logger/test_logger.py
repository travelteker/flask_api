import os

from unittest import TestCase, mock

from app.utils.logger.base_logger import BaseLogger


class TestLogger(TestCase):

    def setUp(self) -> None:
        self.logger = BaseLogger()

    @mock.patch.dict(os.environ, {'DIR_LOGS': 'logs'})
    @mock.patch('app.utils.logger.base_logger.TimedRotatingFileHandler')
    @mock.patch('app.utils.logger.base_logger.logging.getLogger')
    def test_create_logger(self, mock_logger, mock_rotated):
        title = 'dummy'
        mock_logger.return_value.configure_mock(handlers='')
        self.logger.create_logger(title)
        self.assertTrue(mock_logger.called)
        self.assertTrue(mock_rotated.called)



