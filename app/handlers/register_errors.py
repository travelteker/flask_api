from json import loads
from werkzeug.exceptions import NotFound, BadRequest, MethodNotAllowed, InternalServerError
from flask import jsonify, Flask


class CustomRegisterErrorHandler:

    """Class to customize errors HTTP"""

    CUSTOM_HANDLERS = {
        500: 'base_error_handler',
        405: 'method_not_allowed',
        404: 'not_found',
        400: 'bad_request'
    }

    def __init__(self):
        self.__module = type(self).__name__

    def init_app(self, app: Flask):
        for key, method_name in type(self).CUSTOM_HANDLERS.items():
            app.register_error_handler(key, getattr(self, method_name))

    @staticmethod
    def base_error_handler(error: InternalServerError):
        return jsonify({"data": {"error": str(error)}}), 500

    @staticmethod
    def method_not_allowed(error: MethodNotAllowed):
        title, data, *otros = str(error).split(':')
        return jsonify({"data": {"error": data}}), 405

    @staticmethod
    def not_found(error: NotFound):
        title, data, *otros = str(error).split(':')
        return jsonify({"data": {"error": data}}), 404

    @staticmethod
    def bad_request(error: BadRequest):
        limit = '400 Bad Request: '
        info = str(error)[len(limit):]
        detect_char = info.find('{')
        message = info
        if not detect_char:
            message = loads(info.replace("'", '"'))
        return jsonify({"data": {"error": message}}), 400
