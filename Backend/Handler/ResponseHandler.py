import json

from django.http import HttpResponse

from Helper.Constants import *


class SuccessResponse:
    def __init__(self, data=None, text="", title='',
                 status_code=SUCCESS_RESPONSE_CODE):
        if data is None:
            data = {}
        self.data = data
        self.text = text
        self.title = title
        self.status_code = status_code

    def response_object(self):
        return {
            'data': self.data,
            'message': {
                "status": self.status_code,
                "text": self.text,
                "title": self.title
            }
        }

    def return_response_object(self):
        try:
            value_ = json.dumps(self.response_object())
            return respond(value_, self.status_code)
        except Exception as e:
            return FailureResponse('Failed to serialize data').return_response_object()


class FailureResponse:
    def __init__(self, text='Something Went Wrong', title='', status_code=INTERNAL_SERVER_ERROR):
        self.text = text
        self.title = title
        self.status_code = status_code

    def response_object(self):
        return {
            'data': {},
            'message': {
                "status": self.status_code,
                "text": self.text,
                "title": self.title
            }
        }

    def method_not_allowed(self):
        dict_ = {
            'data': {},
            'message': {
                "status": METHOD_NOT_ALLOWED,
                "text": "METHOD_NOT_ALLOWED",
                "title": self.title
            }
        }
        return respond(json.dumps(dict_), METHOD_NOT_ALLOWED)

    def unauthorized_object(self):
        dict_ = {
            'data': {},
            'message': {
                "status": UNAUTHORIZED,
                "text": 'Unauthorized User',
                "title": self.title
            }
        }
        return respond(json.dumps(dict_), UNAUTHORIZED)

    def return_response_object(self):
        return respond(json.dumps(self.response_object()), self.status_code)


def respond(value, status):
    response = HttpResponse(value, content_type='application/json', status=status)
    return response
