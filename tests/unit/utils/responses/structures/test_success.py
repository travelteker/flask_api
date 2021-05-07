from unittest import TestCase
from unittest import mock

from app.utils.responses.structures.success import Success


class TestSuccess(TestCase):

    @mock.patch('app.utils.responses.structures.success.Response')
    def test_response(self, mock_response):
        data = [1, 2, 3]
        Success.response(data)
        self.assertTrue(mock_response.called)

