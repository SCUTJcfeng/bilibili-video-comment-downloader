
import json
from requests import sessions


class HttpMethod:
    GET = 'get'
    POST = 'post'
    DELETE = 'delete'


class RequestUtil:
    session = sessions.Session()

    @classmethod
    def do_request(cls, request):
        response = cls.session.request(method=request.method, url=request.url, params=request.params, timeout=10)
        return cls.build_response(request, response)

    @classmethod
    def build_response(cls, request, raw_response):
        return Response(request=request, raw_response=raw_response)


class Request:
    def __init__(self, url, method=HttpMethod.GET, params=None, data=None):
        self._url = url
        self._method = method
        self._params = params
        self._data = data

    @property
    def url(self):
        return self._url

    @property
    def method(self):
        return self._method

    @property
    def params(self):
        return self._params

    @property
    def data(self):
        return self._data


class Response:
    def __init__(self, request, raw_response):
        self._request = request
        self._raw_response = raw_response
        self._json_data = json.loads(self._raw_response.text)

    @property
    def request(self):
        return self._request

    @property
    def raw_response(self):
        return self._raw_response

    @property
    def status_code(self):
        return self._raw_response.status_code

    @property
    def code(self):
        return self._json_data['code']

    @property
    def data(self):
        return self._json_data['data']

    @property
    def message(self):
        return self._json_data['message']
