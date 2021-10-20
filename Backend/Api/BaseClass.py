import json
import uuid
import asyncio
from Helper.Pagination import Paginate

from django.utils.decorators import classonlymethod
from django.views.generic import View
from asgiref.sync import sync_to_async
from django.urls import path

from Filters.Jwt import JWTClass, connection
from Models.models import LogEntryForException
from Handler.RequestHandler import DecoratorHandler, SuccessResponse

class BaseClass(View):

    def dispatch(self, request, *args, **kwargs):
        path_ = request.path.split('/')[-1]
        handler = getattr(self, path_, self.http_method_not_allowed)
        return handler(request, *args, **kwargs)

    @sync_to_async
    def paginate_response(self, paginate_):
        return paginate_.paginate()

    @staticmethod
    def get_pagination_params(request):
        start_index = request.GET.get('start_index', 0)
        limit = request.GET.get('limit', 10)
        limit = int(limit)
        start_index = int(start_index)
        return start_index, limit

    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    async def check_user_permission(self, request, route_info=None):
        return await self.check_authentication(request, route_info)

    @staticmethod
    @sync_to_async
    def check_authentication(request, route_info):
        token_ = request.META['HTTP_AUTHORIZATION'] if 'HTTP_AUTHORIZATION' in request.META else ''
        if token_:
            response = JWTClass().decode_jwt_token(token_, route_info)
            if response:
                return response
        return False
    
    @staticmethod
    @sync_to_async
    def insert_query(query):
         with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()

    def decode_request_obj(self, request):
        user_agent = self.request.META.get('HTTP_USER_AGENT', '')
        requested_url = self.request.META.get('HTTP_REFERER', '')
        ip_address = self.get_client_ip_address_from_request()
        return user_agent, requested_url, ip_address

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
    def _exception_log_entry(self, request, exception):
        obj = self.decode_request_obj(request)
        LogEntryForException.objects.create(Exception=exception, RequestUrl=obj[1],
                                            UserAgent=obj[1],
                                            IpAddress=obj[2])
        return
