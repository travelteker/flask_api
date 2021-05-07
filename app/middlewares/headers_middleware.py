from typing import Any

from bson import json_util
from werkzeug.wrappers import Request, Response


class HeadersMiddleware:

    """
    WSGI middleware
    """

    def __init__(self, app: Any):
        self.__app = app

    def __call__(self, environ: Any, start_response: Any):
        """Checking headers mandatory, if are not found aborting request"""
        request = Request(environ)
        x_api_key = request.headers.get("X-Api-Key")
        x_version = request.headers.get("X-Api-Version")
        if x_api_key is None or x_version is None:
            body = {'code': 401, 'resp': {'error': 'Headers <X-Api-Key> and <X-Api-Version> are mandatory'}}
            response = json_util.dumps(body)
            resp = Response(response, mimetype='application/json', status=401)
            return resp(environ, start_response)
        return self.__app(environ, start_response)
