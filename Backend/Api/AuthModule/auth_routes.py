from django.urls import path
from .authentication import *

urlpatterns = [
    path('auth/authentication', Authentication.as_view()),

]
