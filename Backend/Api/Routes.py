from django.urls import path
from .AuthModule.api import *

urlpatterns = [
    path('auth/login', login),
    path('auth/register', register),
    path('auth/logout', logout)
]
