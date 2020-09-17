from django.urls import path

from .authentication import *

urlpatterns = [
    path('auth/authentication/login', LoginClass.as_view()),
    path('auth/authentication/register', RegisterClass.as_view()),

]
