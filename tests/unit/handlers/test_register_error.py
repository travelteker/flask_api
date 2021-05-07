from unittest import TestCase, mock

from app.handlers.register_errors import CustomRegisterErrorHandler


class TestRegisterError(TestCase):

    def setUp(self) -> None:
        self.handler = CustomRegisterErrorHandler()

    def tearDown(self) -> None:
        del self.handler

    def test_init_app(self):
        app = mock.Mock()
        self.handler.init_app(app)
        self.assertTrue(app.register_error_handler.called)

    @mock.patch('app.handlers.register_errors.jsonify')
    def test_base_error_handler(self, mock_jsonify):
        result = CustomRegisterErrorHandler.base_error_handler(mock.Mock())
        self.assertIsInstance(result, tuple)
        self.assertEqual(result[1], 500)
        self.assertTrue(mock_jsonify.called)

    @mock.patch('app.handlers.register_errors.jsonify')
    def test_method_not_allowed(self, mock_jsonify):
        error = "dummy:error:extra"
        result = CustomRegisterErrorHandler.method_not_allowed(error)
        self.assertIsInstance(result, tuple)
        self.assertEqual(result[1], 405)
        self.assertTrue(mock_jsonify.called)

    @mock.patch('app.handlers.register_errors.jsonify')
    def test_not_found(self, mock_jsonify):
        error = "dummy:error:extra"
        result = CustomRegisterErrorHandler.not_found(error)
        self.assertIsInstance(result, tuple)
        self.assertEqual(result[1], 404)
        self.assertTrue(mock_jsonify.called)


