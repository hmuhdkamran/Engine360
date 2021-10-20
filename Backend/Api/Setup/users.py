#
#   auther: H.Muhammad Kamran
#   email: hmuhdkamran@gmail.com
#   contact: +92 (313 / 333) 9112 845
#

from Api.BaseClass import *
from Models.models import Users,UserSeller

DRequests = DecoratorHandler()

class UsersController(BaseClass):

    @staticmethod
    def purse(obj):
        return {
    'UserId': str(obj.UserId),'Username': obj.Username,'DisplayName': obj.DisplayName,'Language': obj.Language,'Password': obj.Password,'Salt': obj.Salt,'Status': obj.Status
        }

    @staticmethod
    def purseUserSeller(obj):
        return {
    'UserSellerId': str(obj.UserSellerId),'UserId': str(obj.UserId),'SellerId': str(obj.SellerId)
        }    

    @sync_to_async
    def retrieve_objects(self, items):
        return [self.purse(obj) for obj in items]

    @sync_to_async
    def retrieve_objectsVM(self, items):
        return [self.purseUserSeller(obj) for obj in items]    

    @sync_to_async
    def get_all_function(self):
        return Users.objects.all()

    @sync_to_async
    def find_by_function(self, search_string):
        return Users.objects.filter(UserId__icontains=search_string)


    @sync_to_async
    def find_by_functionUserSeller(self, search_string):
        return UserSeller.objects.filter(UserId__icontains=search_string)     

    @sync_to_async
    def create_update_function(self, data):
        Users.objects.update_or_create(
            UserId=data['UserId'], defaults=dict(UserId=data['UserId'],Username=data['Username'],DisplayName=data['DisplayName'],Language=data['Language'],Password=data['Password'],Salt=data['Salt'],Status=data['Status']))

    @sync_to_async
    def delete_function(self, data):
        Users.objects.filter(UserId=data['UserId']).delete()

    @DRequests.rest_api_call(['GET'], is_authenticated=True, claim='users', operation='R')
    async def getAll(self, request):
        start_index, limit = self.get_pagination_params(request)
        items = await self.get_all_function()
        paginate_ = Paginate(items, self.purse, start_index, limit)
        items = await self.paginate_response(paginate_)
        return SuccessResponse(data=items).return_response_object()

    @DRequests.rest_api_call(['POST'], is_authenticated=True, claim='users',operation='R')
    async def findBy(self, request):
        data = json.loads(request.body.decode('utf-8'))
        items = await self.find_by_function(data['parameter'])
        items = await self.retrieve_objects(items)
        return SuccessResponse(data=items).return_response_object()

    @DRequests.rest_api_call(['POST'], is_authenticated=False, claim='users',operation='R')
    async def findByUserSeller(self, request):
        data = json.loads(request.body.decode('utf-8'))
        items = await self.find_by_functionUserSeller(data['search_string'])
        items = await self.retrieve_objectsVM(items)
        return SuccessResponse(data=items).return_response_object()    

    @DRequests.rest_api_call(['POST'], is_authenticated=True, claim='users', operation='C')
    async def create(self, request):
        await self.create_update_function(json.loads(request.body.decode('utf-8')))
        return SuccessResponse().return_response_object()

    @DRequests.rest_api_call(['PUT'], is_authenticated=True, claim='users', operation='U')
    async def update(self, request):
        await self.create_update_function(json.loads(request.body.decode('utf-8')))
        return SuccessResponse().return_response_object()

    @DRequests.rest_api_call(['POST'], is_authenticated=True, claim='users',operation='D')
    async def delete(self, request):
        await self.delete_function(json.loads(request.body.decode('utf-8')))
        return SuccessResponse().return_response_object()

urlpatterns = [
    path('users/getAll', UsersController.as_view()),
    path('users/findBy', UsersController.as_view()),
    path('users/findByUserSeller', UsersController.as_view()),
    path('users/create', UsersController.as_view()),
    path('users/update', UsersController.as_view()),
    path('users/delete', UsersController.as_view()),
]