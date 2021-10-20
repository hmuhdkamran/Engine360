from functools import wraps

from asgiref.sync import sync_to_async, async_to_sync
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

    @sync_to_async
    def _exception_log_entry(self, exception):
        LogEntryForException.objects.create(Exception=exception, RequestUrl=self.requested_url,
                                            UserAgent=self.user_agent,
                                            IpAddress=self.ip_address)
        return


class DecoratorHandler:

    @staticmethod
    @sync_to_async
    def authentication_level(request, claim, operation):
        # request_path = request.path.split('/')[-2]
        token_ = request.META['HTTP_AUTHORIZATION'] if 'HTTP_AUTHORIZATION' in request.META else ''
        if token_:
            route_info = {'RouteName': claim, 'Operation': operation}
            response = JWTClass().decode_jwt_token(token_, route_info)
            if response:
                return response
        return False

    def return_http_response(self, response):
        return response

    def rest_api_call(self, allowed_method_list, is_authenticated=False, operation='', claim=''):
        def decorator(view):
            @csrf_exempt
            @wraps(view)
            async def wrapper(request, *args, **kwargs):
                request_handler = RequestHandler(request)

                if request.request.method in allowed_method_list:
                    if is_authenticated:
                        user_ = await self.authentication_level(request.request,claim, operation)
                        if user_:
                            request.request.user = user_
                            try:
                                response = await view(request, *args, **kwargs)
                            except Exception as e:
                                print (e)
                                await request_handler._exception_log_entry(e)
                                response = self.return_http_response(FailureResponse(text=str(e)).return_response_object())
                        else:
                            response = self.return_http_response(FailureResponse().unauthorized_object())
                    else:
                        print ("not authenaticated flow rewiuts handler scenario")
                        try:
                            response = await view(request, *args, **kwargs)
                        except Exception as e:
                            print (e)
                            # await request_handler._exception_log_entry(e)
                            response = self.return_http_response(FailureResponse(text=str(e)).return_response_object())
                else:
                    response = self.return_http_response(FailureResponse().method_not_allowed())
                return response

            return wrapper

        return decorator


def method_decorator_adaptor(adapt_to, *decorator_args, **decorator_kwargs):
    def decorator_outer(func):
        @wraps(func)
        def decorator(self, *args, **kwargs):
            @adapt_to(*decorator_args, **decorator_kwargs)
            def adaptor(*args, **kwargs):
                return func(self, *args, **kwargs)
            return adaptor(*args, **kwargs)
        return decorator
    return decorator_outer