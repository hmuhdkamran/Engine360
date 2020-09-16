from django.urls import path
from .authentication import *

urlpatterns = [
    path('auth/authentication/login', Authentication.as_view({'post': 'post_login'})),
    path('auth/authentication/register', Authentication.as_view({'post': 'post_register'})),

]
