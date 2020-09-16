import json

from django.views import View
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from Filters.Jwt import JWTClass
from Handler.PasswordHandler import Hashing
from Handler.RequestHandler import DecoratorHandler, FailureResponse, SuccessResponse
from Helper.Constants import *
from Helper.Utils import *
from Models.models import User
from django.utils.decorators import classonlymethod
from functools import update_wrapper

DRequests = DecoratorHandler()


class Authentication(GenericViewSet):

    # @DRequests.rest_api_call(['PUT'])
    def post_login(self, request):
        data = json.loads(request.body.decode('utf-8'))
        email = data['username'].lower().strip()
        password = data['password']

        user_ = User.objects.filter(Username=email).last()
        if user_:
            if Hashing()._compare_stored_hash(password, user_.Salt, user_.Password):
                data = JWTClass().create_user_session(user_)
                return SuccessResponse(data={"access_token": data, "expires_on": 360}).return_response_object()

        return FailureResponse(text='Username or password is incorrect.',
                               status_code=BAD_REQUEST_CODE).return_response_object()

    # @DRequests.rest_api_call(['POST'])
    def post_register(self, request):
        data = json.loads(request.body.decode('utf-8'))
        email = data['username'].strip().lower()
        password = data['password'].strip()
        confirm_password = data['confirm_password'].strip()
        name = data['name'].strip()
        language = data['language'].strip() if 'language' in data else 'English'

        if not check_email_validation(email):
            return FailureResponse(text='Please type valid email address',
                                   status_code=BAD_REQUEST_CODE).return_response_object()

        if password != confirm_password:
            return FailureResponse(text='Password doesnt match',
                                   status_code=BAD_REQUEST_CODE).return_response_object()

        if User.objects.filter(Username=email).exists():
            return FailureResponse(text='Email already exists',
                                   status_code=BAD_REQUEST_CODE).return_response_object()

        hash_pass, salt = Hashing().generate_password(password)

        user_ = User.objects.create(Username=email, Password=hash_pass, DisplayName=name, Language=language,
                                    Salt=salt, Status=True)

        data = JWTClass().create_user_session(user_)
        return SuccessResponse(data=data, text='User Created Successfully!').return_response_object()


class UserViewSet(APIView):
    pass