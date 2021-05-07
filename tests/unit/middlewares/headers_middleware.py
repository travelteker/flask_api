from unittest import TestCase, mock
from unittest.mock import PropertyMock

from app.middlewares.headers_middleware import HeadersMiddleware


class TestHeadersMiddleware(TestCase):

    @mock.patch('app.middlewares.headers_middleware.Response')
    @mock.patch('app.middlewares.headers_middleware.Request')
    def test_call_middleware_failure_headers(self, mock_req, mock_resp):
        app = mock.Mock()
        mock_req.return_value.headers = {}
        middle = HeadersMiddleware(app)
        environ = mock.Mock()
        start_response = mock.Mock()
        middle(environ, start_response)
        self.assertTrue(mock_resp.called)

    @mock.patch('app.middlewares.headers_middleware.Request')
    def test_call_middleware_success(self, mock_req):
        app = mock.Mock()
        mock_req.return_value.headers = {
            'X-Api-Key': 123456,
            'X-Api-Version': 2
        }
        middle = HeadersMiddleware(app)
        environ = mock.Mock()
        start_response = mock.Mock()
        middle(environ, start_response)
        self.assertTrue(app.called)
