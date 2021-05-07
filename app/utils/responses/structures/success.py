from json import dumps
from typing import Any
from flask import Response


class Success:

    @staticmethod
    def response(data: Any = None, code: int = 200) -> Response:
        """Prepare structure data to send with <success> responses
        :param data: Optional[Any] Data to send in response
        :param code: (int) Status code for response in range 2xx
        :return: (Response)
        """
        aux = data
        if isinstance(data, list):
            aux = {'data': data}
        casting = dumps(aux)
        return Response(casting, status=code, mimetype='application/json')

