from os import sep, getcwd
from flask import Flask

from app.middlewares.headers_middleware import HeadersMiddleware
from app.utils.conditions.base import Base as ContainerConditions
from app.models import mongo_db
from app.handlers.register_errors import CustomRegisterErrorHandler
from app.routes import register_routes
from app.handlers.logger_req_res import LoggerReqRes


class Main:

    def __init__(self):
        self.__module = type(self).__module__
        self.__conditions = ContainerConditions().apply_conditions()
        self.__error_handlers = CustomRegisterErrorHandler()
        self.__logger = LoggerReqRes()

    def create_app(self, config_file='settings.py') -> Flask:
        try:
            app = Flask(__name__)
            app.config.from_pyfile(sep.join([getcwd(), 'app', 'config', config_file]))
            self.__logger.init_app(app)
            mongo_db.init_app(app)
            type(self).register_middlewares(app)
            register_routes(app)
            self.__error_handlers.init_app(app)
            return app
        except Exception as err:
            exit(f'Bootstrap Flask server failure|description: {err}')

    @staticmethod
    def register_middlewares(app: Flask):
        app.wsgi_app = HeadersMiddleware(app.wsgi_app)

    def run(self, **params):
        context = self.create_app()
        context.run(**params)

