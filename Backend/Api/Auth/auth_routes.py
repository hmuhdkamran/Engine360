from django.urls import path

from.authentication import *

urlpatterns = [
    path('auth/login', LoginClass.as_view()),
    path('auth/register', RegisterClass.as_view()),

]
