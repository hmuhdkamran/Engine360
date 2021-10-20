#
#   auther: H.Muhammad Kamran
#   email: hmuhdkamran@gmail.com
#   contact: +92 (313 / 333) 9112 845
#

from Api.BaseClass import *
from Models.models import RolesRoutesMap

DRequests = DecoratorHandler()

class RolesRoutesMapController(BaseClass):

    @staticmethod
    def purse(obj):
        return {
    'RoleRouteMapId': str(obj.RoleRouteMapId),'RoleId': str(obj.RoleId),'RouteId': str(obj.RouteId),'Status': obj.Status,'Operation': obj.Operation
        }

    @sync_to_async
    def retrieve_objects(self, items):
        return [self.purse(obj) for obj in items]

    @sync_to_async
    def get_all_function(self):
        return RolesRoutesMap.objects.all()

    @sync_to_async
    def find_by_function(self, search_string):
        return RolesRoutesMap.objects.filter(RoleRouteMapId__icontains=search_string)

    @sync_to_async
    def create_update_function(self, data):
        RolesRoutesMap.objects.update_or_create(
            RoleRouteMapId=data['RoleRouteMapId'], defaults=dict(RoleRouteMapId=data['RoleRouteMapId'],RoleId=data['RoleId'],RouteId=data['RouteId'],Status=data['Status'],Operation=data['Operation']))

    @sync_to_async
    def delete_function(self, data):
        RolesRoutesMap.objects.filter(RoleRouteMapId=data['RoleRouteMapId']).delete()

    @DRequests.rest_api_call(['GET'], is_authenticated=True, claim='rolesroutesmap', operation='R')
    async def getAll(self, request):
        start_index, limit = self.get_pagination_params(request)
        items = await self.get_all_function()
        paginate_ = Paginate(items, self.purse, start_index, limit)
        items = await self.paginate_response(paginate_)
        return SuccessResponse(data=items).return_response_object()

    @DRequests.rest_api_call(['POST'], is_authenticated=True, claim='rolesroutesmap',operation='R')
    async def findBy(self, request):
        data = json.loads(request.body.decode('utf-8'))
        items = await self.find_by_function(data['parameter'])
        items = await self.retrieve_objects(items)
        return SuccessResponse(data=items).return_response_object()

    @DRequests.rest_api_call(['POST'], is_authenticated=True, claim='rolesroutesmap', operation='C')
    async def create(self, request):
        await self.create_update_function(json.loads(request.body.decode('utf-8')))
        return SuccessResponse().return_response_object()

    @DRequests.rest_api_call(['PUT'], is_authenticated=True, claim='rolesroutesmap', operation='U')
    async def update(self, request):
        await self.create_update_function(json.loads(request.body.decode('utf-8')))
        return SuccessResponse().return_response_object()

    @DRequests.rest_api_call(['POST'], is_authenticated=True, claim='rolesroutesmap',operation='D')
    async def delete(self, request):
        await self.delete_function(json.loads(request.body.decode('utf-8')))
        return SuccessResponse().return_response_object()

urlpatterns = [
    path('rolesroutesmap/getAll', RolesRoutesMapController.as_view()),
    path('rolesroutesmap/findBy', RolesRoutesMapController.as_view()),
    path('rolesroutesmap/create', RolesRoutesMapController.as_view()),
    path('rolesroutesmap/update', RolesRoutesMapController.as_view()),
    path('rolesroutesmap/delete', RolesRoutesMapController.as_view()),
]