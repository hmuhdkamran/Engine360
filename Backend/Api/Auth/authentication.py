import redis
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from Api.BaseClass import *
from Filters.Jwt import JWTClass
from Handler.PasswordHandler import Hashing
from Handler.RequestHandler import DecoratorHandler, FailureResponse, SuccessResponse
from Helper.Constants import *
from Helper.Utils import *
from Models.models import *

import uuid


DRequests = DecoratorHandler()

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0)


class Authentication(BaseClass):

    @sync_to_async
    def get_user_obj(self, email):
        return Users.objects.filter(Username=email).last()

    @sync_to_async
    def logout_token(self, token_):
        return JWTClass().decode_jwt_token_and_logout(token_)

    @sync_to_async
    def get_user_token(self, user_):
        return JWTClass().create_user_session(user_)

    async def login(self, request):
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

    @sync_to_async
    def check_email_exists(self, email):
        if Users.objects.filter(Username=email).exists():
            return FailureResponse(text='Email already exists',
                                   status_code=BAD_REQUEST_CODE).return_response_object()
        else:
            return False

    @sync_to_async
    def create_a_new_user(self, email, hash_pass, name, language, salt, status):
        user_= Users.objects.create(Username=email, Password=hash_pass, DisplayName=name, Language=language,
                                   Salt=salt, Status=status, UserId=uuid.uuid4())
        print (user_)
        return user_

    @sync_to_async
    def create_user_role_entries(self, user):
        roles_ = RolesRoutesMap.objects.filter(RoleId__FullName='User')
        # user_role_map = [UsersRolesMap(UserId=user, RoleRouteMapId=x, Status=True) for x in roles_]


        # print (roles_)
        for x in roles_:
            try:
                UsersRolesMap.objects.create(UserId=user, RoleRouteMapId=x, Status=True)
            except Exception as e:
                print (e)
        # UsersRolesMap.objects.bulk_create(user_role_map)

    @DRequests.rest_api_call(allowed_method_list=['POST'])
    async def register(self, request):
        data = json.loads(request.body.decode('utf-8'))
        email = data['username'].strip().lower()
        password = data['password'].strip()
        confirm_password = data['confirmPassword'].strip()
        name = data['displayName'].strip()
        language = data['language'].strip() if 'language' in data else 'en-US'

        # if not check_email_validation(email):
        #     return FailureResponse(text='Please type valid email address',
        #                            status_code=BAD_REQUEST_CODE).return_response_object()

        if password != confirm_password:
            return FailureResponse(text='Password doesnt match',
                                   status_code=BAD_REQUEST_CODE).return_response_object()

        email_exists = await self.check_email_exists(email)
        if email_exists:
            return FailureResponse(text='Email/Contact already exists',
                                   status_code=BAD_REQUEST_CODE).return_response_object()

        hash_pass, salt = Hashing().generate_password(password)

        user_ = await self.create_a_new_user(email, hash_pass, name, language, salt, True)      
        print (type(user_))  
        await self.create_user_role_entries(user_)

        return SuccessResponse(data={}, text='User Created Successfully!').return_response_object()

    @DRequests.rest_api_call(allowed_method_list=['PUT'], is_authenticated=False)
    async def logout(self, request):
        token_ = request.META['HTTP_AUTHORIZATION']
        await self.logout_token(token_)
        return SuccessResponse(data={}, text='Logout').return_response_object()


urlpatterns = [
    path('auth/login', Authentication.as_view()),
    path('auth/register', Authentication.as_view()),
    path('auth/logout', Authentication.as_view()),

]
