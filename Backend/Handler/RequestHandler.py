from functools import wraps

from django.views.decorators.csrf import csrf_exempt

from Filters.Jwt import *
from .ResponseHandler import *
from Models.models import LogEntryForException


class RequestHandler:
    def __init__(self, request):
        self.request = request.request
        self.user_agent = self.request.META.get('HTTP_USER_AGENT', '')
        self.requested_url = self.request.META.get('HTTP_REFERER', '')
        self.ip_address = self.get_client_ip_address_from_request()
        self.get_client_ip_address_from_request()

    def get_client_ip_address_from_request(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip_address = x_forwarded_for.split(',')[0]
        else:
            ip_address = self.request.META.get('REMOTE_ADDR')
        if not ip_address:
            ip_address = ''
        return ip_address

    def _exception_log_entry(self, exception):
        LogEntryForException.objects.create(Exception=exception, RequestUrl=self.requested_url,
                                            UserAgent=self.user_agent,
                                            IpAddress=self.ip_address)
        return


class DecoratorHandler:
    @staticmethod
    def authentication_level(request, authentication_level):
        token_ = request.META['HTTP_AUTHORIZATION'] if 'HTTP_AUTHORIZATION' in request.META else ''
        if token_:
            response = JWTClass().decode_jwt_token(token_, authentication_level)
            if response:
                return response
        return False

    def rest_api_call(self, allowed_method_list, is_authenticated=False, authentication_level=None):
        def decorator(view):
            @csrf_exempt
            @wraps(view)
            def wrapper(request, *args, **kwargs):
                request_handler = RequestHandler(request)
                if request.request.method in allowed_method_list:
                    if is_authenticated:
                        user_ = self.authentication_level(request.request, authentication_level)
                        if user_:
                            request.user = user_
                            try:
                                response = view(request.request, *args, **kwargs)
                            except Exception as e:
                                request_handler._exception_log_entry(e)
                                response = FailureResponse().return_response_object()
                        else:
                            response = FailureResponse().unauthorized_object()
                    else:
                        try:
                            response = view(request, *args, **kwargs)
                        except Exception as e:
                            request_handler._exception_log_entry(e)
                            response = FailureResponse().return_response_object()
                else:
                    response = FailureResponse().method_not_allowed()
                return response

            return wrapper

        return decorator
