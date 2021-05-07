from flask import Flask, request, Response

from app.utils.logger.base_logger import BaseLogger


class LoggerReqRes:

    """Class to register info before and after requests"""

    def __init__(self):
        self.__module = type(self).__name__
        self.__logger = BaseLogger().create_logger(self.__module)

    def init_app(self, app: Flask):
        """Method factory to initialize options before and after request
        :params app: (Flask) Instance application
        :return: (None)
        """
        app.before_request(self.before_request)
        app.after_request(self.after_request)

    def before_request(self):
        """Method to apply before of process request"""
        method = request.method
        path = request.path
        endpoint = request.endpoint
        ip = request.environ.get("REMOTE_ADDR")
        body = request.data
        self.__logger.debug(f'{self.__module}|before_request()|method: {method}|path: {path}|blueprint: {endpoint}'
                            f'|IP: {ip}|body: {body}')

    def after_request(self, response: Response):
        """Method to apply after of process request"""
        body = response.get_data()
        self.__logger.debug(f'{self.__module}|after_request()|body:{body}')
        return response
