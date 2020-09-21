import json

from asgiref.sync import sync_to_async

from Api.BaseClass import BaseClass
from Filters.Jwt import JWTClass
from Handler.PasswordHandler import Hashing
from Handler.RequestHandler import DecoratorHandler, FailureResponse, SuccessResponse
from Helper.Constants import *
from Helper.Utils import *
from Models.models import User

DRequests = DecoratorHandler()

class LoginClass(BaseClass):

    @sync_to_async
    def get_user_obj(self, email):
        return User.objects.filter(Username=email).last()

    @sync_to_async
    def get_user_token(self, user_):
        return JWTClass().create_user_session(user_)

    async def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        email = data['username'].lower().strip()
        password = data['password']

        user_ = await self.get_user_obj(email)

        if user_:
            if Hashing()._compare_stored_hash(password, user_.Salt, user_.Password):
                data = await self.get_user_token(user_)
                return SuccessResponse(data={"access_token": data, "expires_on": 360}).return_response_object()

        return FailureResponse(text='Username or password is incorrect.',
                               status_code=BAD_REQUEST_CODE).return_response_object()


class RegisterClass(BaseClass):

    @sync_to_async
    def check_email_exists(self, email):
        if User.objects.filter(Username=email).exists():
            return FailureResponse(text='Email already exists',
                                   status_code=BAD_REQUEST_CODE).return_response_object()
        else:
            return False

    @sync_to_async
    def create_a_new_user(self, email, hash_pass, name, language, salt, status):
        return User.objects.create(Username=email, Password=hash_pass, DisplayName=name, Language=language,
                                   Salt=salt, Status=status)

    @sync_to_async
    def create_user_session(self, user_):
        return JWTClass().create_user_session(user_)

    async def post(self, request):
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

        email_exists = await self.check_email_exists(email)
        if email_exists:
            return email_exists

        hash_pass, salt = Hashing().generate_password(password)

        user_ = await self.create_a_new_user(email, hash_pass, name, language, salt, True)

        data = await self.create_user_session(user_)
        return SuccessResponse(data=data, text='User Created Successfully!').return_response_object()
