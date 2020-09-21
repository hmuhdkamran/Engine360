import asyncio

from django.utils.decorators import classonlymethod
from django.views.generic import View


class BaseClass(View):

    @classonlymethod
    def as_view(cls, actions=None, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view
