from unittest import TestCase, mock

from app.handlers.logger_req_res import LoggerReqRes


class TestLoggerReqRes(TestCase):

    @mock.patch('app.handlers.logger_req_res.BaseLogger')
    def setUp(self, mock_logger) -> None:
        self.logger = LoggerReqRes()

    def tearDown(self) -> None:
        del self.logger

    def test_init_app(self):
        app = mock.Mock()
        self.logger.init_app(app)
        self.assertTrue(app.before_request.called)
        self.assertTrue(app.after_request.called)

    @mock.patch('app.handlers.logger_req_res.Response')
    def test_after_request(self, mock_response):
        resp = mock.Mock()
        self.logger.after_request(resp)
        self.assertTrue(resp.get_data.called)
