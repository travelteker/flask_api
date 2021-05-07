from typing import Any

from flask import Response, jsonify


class JsonResponse(Response):

    """Class to modify any response adding a default structure in body before response
    This class can be used in <main.py> in method <__create_app()> adding this parameter
    <app.response_class = JsonResponse>
    Only indicate the object class and not the instance object
    From a <classmethod> can be called others functions in class when this functions are statics
    It's necessary modify object Response to change body of response.
    """

    @classmethod
    def force_type(cls, data: Any, environ = None):
        if isinstance(data, dict):
            data = jsonify(data)
        return super(Response, cls).force_type(data, environ)
