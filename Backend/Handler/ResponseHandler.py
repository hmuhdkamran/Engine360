import json
from uuid import UUID

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
                "messageTypeId": self.status_code,
                "text": self.text,
                "title": self.title
            }
        }

    def return_response_object(self):
        try:
            value_ = json.dumps(self.response_object(),indent=4,default=uuid_convert)
            return respond(value_)
        except Exception as e:
            print (e)
            return FailureResponse('Failed to serialize data').return_response_object()


class FailureResponse:
    def __init__(self, text='Something Went Wrong', title='', status_code=INTERNAL_SERVER_ERROR):
        self.text = text
        self.title = title
        self.status_code = status_code

    def response_object(self):
        print (self.text)
        return {
            'data': {},
            'message': {
                "messageTypeId": self.status_code,
                "text": self.text,
                "title": self.title
            }
        }

    def method_not_allowed(self):
        dict_ = {
            'data': {},
            'message': {
                "messageTypeId": METHOD_NOT_ALLOWED,
                "text": "METHOD_NOT_ALLOWED",
                "title": self.title
            }
        }
        return respond(json.dumps(dict_))

    def unauthorized_object(self):
        dict_ = {
            'data': {},
            'message': {
                "messageTypeId": UNAUTHORIZED,
                "text": 'Unauthorized User',
                "title": self.title
            }
        }
        return respond(json.dumps(dict_))

    def bad_url_object(self):
        dict_ = {
            'data': {},
            'message': {
                "messageTypeId": PAGE_NOT_FOUND,
                "text": 'Page not found',
                "title": self.title
            }
        }
        return respond(json.dumps(dict_))

    def something_went_wrong(self):
        dict_ = {
            'data': {},
            'message': {
                "messageTypeId": INTERNAL_SERVER_ERROR,
                "text": self.text,
                "title": self.title
            }
        }
        return respond(json.dumps(dict_))

    def return_response_object(self):
        return respond(json.dumps(self.response_object()))

def uuid_convert(o):
        if isinstance(o, UUID):
            return o.hex        

def respond(value):
    response = HttpResponse(value, content_type='application/json', status=200)
    return response
