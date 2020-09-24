from django.urls import path

from.authentication import *

urlpatterns = [
    path('auth/login', Authentication.as_view()),
    path('auth/register', Authentication.as_view()),
    path('auth/logout', Authentication.as_view()),

]
