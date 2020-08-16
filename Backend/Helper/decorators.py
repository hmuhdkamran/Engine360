import json
from functools import wraps

import jwt
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Models.models import *
from .constants import *


def respond(value):
    json_string = json.dumps(value)
    response = HttpResponse(json_string, content_type='application/json', status=SUCCESS_RESPONSE_CODE)
    return response


def public_rest_call(allowed_method_list=None):
    def decorator(view):
        @csrf_exempt
        @wraps(view)
        def wrapper(request, *args, **kwargs):
            if request.method in allowed_method_list:
                data_ = view(request, *args, **kwargs)
                response = return_class(data_)
                response = respond(response)
            else:
                dictionary = {
                    'message': 'Method Not Allowed',
                    'status': METHOD_NOT_ALLOWED
                }
                response = return_class(dictionary)
                response = respond(response)
            return response

        return wrapper

    return decorator


def authenticated_rest_call(allowed_method_list=None):
    def decorator(view):
        @csrf_exempt
        @wraps(view)
        def wrapper(request, *args, **kwargs):
            if request.method in allowed_method_list:
                token = request.META['HTTP_AUTHORIZATION'] if 'HTTP_AUTHORIZATION' in request.META else None
                if token is None:
                    dictionary = {
                        'data': {},
                        'message': 'Unauthorized',
                        'status': UNAUTHORIZED
                    }
                    response = return_class(dictionary)
                    response = respond(response)
                    return response
                response_ = token_validation(token)
                if response_:
                    request.user = response_['user']
                    request.profile = response_['profile']
                    data_ = view(request, *args, **kwargs)
                    response = return_class(data_)
                    response = respond(response)
                else:
                    dictionary = {
                        'data': {},
                        'message': 'Unauthorized',
                        'status': UNAUTHORIZED
                    }
                    response = return_class(dictionary)
                    response = respond(response)
            else:
                dictionary = {
                    'data': {},
                    'message': 'Method Not Allowed',
                    'status': METHOD_NOT_ALLOWED
                }
                response = return_class(dictionary)
                response = respond(response)
            return response

        return wrapper

    return decorator


def authenticated_rest_call_influencer(allowed_method_list=None):
    def decorator(view):
        @csrf_exempt
        @wraps(view)
        def wrapper(request, *args, **kwargs):
            if request.method in allowed_method_list:
                token = request.META['HTTP_AUTHORIZATION'] if 'HTTP_AUTHORIZATION' in request.META else None
                if token is None:
                    dictionary = {
                        'data': {},
                        'message': 'Unauthorized',
                        'status': UNAUTHORIZED
                    }
                    response = return_class(dictionary)
                    response = respond(response)
                    return response
                response_ = token_validation(token)
                if response_:
                    if response_['profile'].role != 0:
                        dictionary = {
                            'data': {},
                            'message': 'Unauthorized',
                            'status': UNAUTHORIZED
                        }
                        response = return_class(dictionary)
                        response = respond(response)
                        return response
                    request.user = response_['user']
                    request.profile = response_['profile']
                    data_ = view(request, *args, **kwargs)
                    response = return_class(data_)
                    response = respond(response)
                else:
                    dictionary = {
                        'data': {},
                        'message': 'Unauthorized',
                        'status': UNAUTHORIZED
                    }
                    response = return_class(dictionary)
                    response = respond(response)
            else:
                dictionary = {
                    'data': {},
                    'message': 'Method Not Allowed',
                    'status': METHOD_NOT_ALLOWED
                }
                response = return_class(dictionary)
                response = respond(response)
            return response

        return wrapper

    return decorator


def authenticated_rest_call_brand(allowed_method_list=None):
    def decorator(view):
        @csrf_exempt
        @wraps(view)
        def wrapper(request, *args, **kwargs):
            if request.method in allowed_method_list:
                token = request.META['HTTP_AUTHORIZATION'] if 'HTTP_AUTHORIZATION' in request.META else None
                if token is None:
                    dictionary = {
                        'data': {},
                        'message': 'Unauthorized',
                        'status': UNAUTHORIZED
                    }
                    response = return_class(dictionary)
                    response = respond(response)
                    return response
                response_ = token_validation(token)
                if response_:
                    if response_['profile'].role != 1:
                        dictionary = {
                            'data': {},
                            'message': 'Unauthorized',
                            'status': UNAUTHORIZED
                        }
                        response = return_class(dictionary)
                        response = respond(response)
                        return response
                    request.user = response_['user']
                    request.profile = response_['profile']
                    data_ = view(request, *args, **kwargs)
                    response = return_class(data_)
                    response = respond(response)
                else:
                    dictionary = {
                        'data': {},
                        'message': 'Unauthorized',
                        'status': UNAUTHORIZED
                    }
                    response = return_class(dictionary)
                    response = respond(response)
            else:
                dictionary = {
                    'data': {},
                    'message': 'Method Not Allowed',
                    'status': METHOD_NOT_ALLOWED
                }
                response = return_class(dictionary)
                response = respond(response)
            return response

        return wrapper

    return decorator


def get_client_ip_address_from_request(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')
    if not ip_address:
        ip_address = ''
    requested_url = request.META.get('HTTP_REFERER', None)
    user_agent = request.META.get('HTTP_USER_AGENT', None)
    return ip_address, requested_url, user_agent


def token_validation(token):
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY_JWT, algorithm=[settings.ALGORITHM_JWT])
        user_ = User.objects.get(id=int(decoded_token['user_id']))
        if user_:
            dictionary = {'user': user_}
            return dictionary
        else:
            return False
    except Exception as e:
        return False


def return_class(dictionary):
    data = dictionary['data'] if 'data' in dictionary else None
    message = dictionary['message']
    status_code = dictionary['status']
    meta = {'message': message, 'status': status_code}
    if data:
        return {'data': data, 'meta': meta}
    else:
        return {'data': {}, 'meta': meta}
