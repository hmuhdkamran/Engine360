import asyncio

from django.utils.decorators import classonlymethod
from django.views.generic import View
from asgiref.sync import sync_to_async

from Filters.Jwt import JWTClass
from Models.models import LogEntryForException


class BaseClass(View):

    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    async def check_user_permission(self, request):
        return await self.check_authentication(request)

    @staticmethod
    @sync_to_async
    def check_authentication(request):
        token_ = request.META['HTTP_AUTHORIZATION'] if 'HTTP_AUTHORIZATION' in request.META else ''
        if token_:
            response = JWTClass().decode_jwt_token(token_)
            if response:
                return response
        return False

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
