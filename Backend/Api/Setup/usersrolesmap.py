#
#   auther: H.Muhammad Kamran
#   email: hmuhdkamran@gmail.com
#   contact: +92 (313 / 333) 9112 845
#

from Api.BaseClass import *
from Models.models import UsersRolesMap,VwUsersRolesMap

DRequests = DecoratorHandler()

class UsersRolesMapController(BaseClass):

    @staticmethod
    def purse(obj):
        return {
    'UserRoleMapId': str(obj.UserRoleMapId),'UserId': str(obj.UserId),'RoleRouteMapId': str(obj.RoleRouteMapId),'Status': obj.Status
        }

    @staticmethod
    def purseVM(obj):
        return {
    'UserRoleMapId': str(obj.UserRoleMapId),'UserId': str(obj.UserId),'RoleRouteMapId': str(obj.RoleRouteMapId),'Status': obj.Status,'DisplayName': obj.DisplayName,'Operation': obj.Operation,'Role': obj.Role,'RouteName': obj.RouteName,'RoleId': str(obj.RoleId),'RouteId': str(obj.RouteId)
        }    

    @sync_to_async
    def retrieve_objects(self, items):
        return [self.purse(obj) for obj in items]

    @sync_to_async
    def retrieve_objectsVM(self, items):
        return [self.purseVM(obj) for obj in items]    

    @sync_to_async
    def get_all_function(self):
        return UsersRolesMap.objects.all()

    @sync_to_async
    def find_by_function(self, search_string):
        return UsersRolesMap.objects.filter(UserRoleMapId__icontains=search_string)

    @sync_to_async
    def find_by_functionVM(self, search_string):
        return VwUsersRolesMap.objects.filter(UserId__icontains=search_string)    

    @sync_to_async
    def create_update_function(self, data):
        UsersRolesMap.objects.update_or_create(
            UserRoleMapId=data['UserRoleMapId'], defaults=dict(UserRoleMapId=data['UserRoleMapId'],UserId=data['UserId'],RoleRouteMapId=data['RoleRouteMapId'],Status=data['Status']))

    @sync_to_async
    def delete_function(self, data):
        UsersRolesMap.objects.filter(UserRoleMapId=data['UserRoleMapId']).delete()

    @DRequests.rest_api_call(['GET'], is_authenticated=True, claim='usersrolesmap', operation='R')
    async def getAll(self, request):
        start_index, limit = self.get_pagination_params(request)
        items = await self.get_all_function()
        paginate_ = Paginate(items, self.purse, start_index, limit)
        items = await self.paginate_response(paginate_)
        return SuccessResponse(data=items).return_response_object()

    @DRequests.rest_api_call(['POST'], is_authenticated=True, claim='usersrolesmap',operation='R')
    async def findBy(self, request):
        data = json.loads(request.body.decode('utf-8'))
        items = await self.find_by_function(data['search_string'])
        items = await self.retrieve_objects(items)
        return SuccessResponse(data=items).return_response_object()

    @DRequests.rest_api_call(['POST'], is_authenticated=True, claim='usersrolesmap',operation='R')
    async def findByUser(self, request):
        data = json.loads(request.body.decode('utf-8'))
        items = await self.find_by_functionVM(data['search_string'])
        items = await self.retrieve_objectsVM(items)
        return SuccessResponse(data=items).return_response_object()    

    @DRequests.rest_api_call(['POST'], is_authenticated=True, claim='usersrolesmap', operation='C')
    async def create(self, request):
        await self.create_update_function(json.loads(request.body.decode('utf-8')))
        return SuccessResponse().return_response_object()

    @DRequests.rest_api_call(['PUT'], is_authenticated=True, claim='usersrolesmap', operation='U')
    async def update(self, request):
        await self.create_update_function(json.loads(request.body.decode('utf-8')))
        return SuccessResponse().return_response_object()

    @DRequests.rest_api_call(['POST'], is_authenticated=True, claim='usersrolesmap',operation='D')
    async def delete(self, request):
        await self.delete_function(json.loads(request.body.decode('utf-8')))
        return SuccessResponse().return_response_object()

urlpatterns = [
    path('usersrolesmap/getAll', UsersRolesMapController.as_view()),
    path('usersrolesmap/findBy', UsersRolesMapController.as_view()),
    path('usersrolesmap/create', UsersRolesMapController.as_view()),
    path('usersrolesmap/update', UsersRolesMapController.as_view()),
    path('usersrolesmap/delete', UsersRolesMapController.as_view()),
    path('usersrolesmap/findByUser', UsersRolesMapController.as_view()),
]