#
#   auther: H.Muhammad Kamran
#   email: hmuhdkamran@gmail.com
#   contact: +92 (313 / 333) 9112 845
#

from Api.BaseClass import *
from Models.models import Roles

DRequests = DecoratorHandler()

class RolesController(BaseClass):

    @staticmethod
    def purse(obj):
        return {
            'RoleId': str(obj.RoleId),
            'ParentRoleId': str(obj.ParentRoleId),
            'FullName': obj.FullName,
            'Status': obj.Status
        }

    @sync_to_async
    def retrieve_objects(self, items):
        return [self.purse(obj) for obj in items]

    @sync_to_async
    def get_all_function(self):
        return Roles.objects.all()

    @sync_to_async
    def find_by_function(self, search_string):
        return Roles.objects.filter(FullName__icontains=search_string)

    @sync_to_async
    def create_update_function(self, data):
        Roles.objects.update_or_create(
            RoleId=data['RoleId'], defaults=dict(
                ParentRoleId=data['ParentRoleId'] if data['ParentRoleId'] != "" else None,
                FullName=data['FullName'],
                Status=True if data['Status'] == 'true' else False))

    @sync_to_async
    def delete_function(self, data):
        Roles.objects.filter(RoleId=data['RoleId']).delete()

    @DRequests.rest_api_call(['GET'], is_authenticated=True, claim='roles', operation='R')
    async def getAll(self, request):
        start_index, limit = self.get_pagination_params(request)
        items = await self.get_all_function()
        paginate_ = Paginate(items, self.purse, start_index, limit)
        items = await self.paginate_response(paginate_)
        return SuccessResponse(data=items).return_response_object()

    @DRequests.rest_api_call(['POST'], is_authenticated=True, claim='roles', operation='R')
    async def findBy(self, request):
        data = json.loads(request.body.decode('utf-8'))
        items = await self.find_by_function(data['parameter'])
        items = await self.retrieve_objects(items)
        return SuccessResponse(data=items).return_response_object()

    @DRequests.rest_api_call(['POST'], is_authenticated=True, claim='roles', operation='C')
    async def create(self, request):
        await self.create_update_function(json.loads(request.body.decode('utf-8')))
        return SuccessResponse().return_response_object()

    @DRequests.rest_api_call(['POST'], is_authenticated=False, claim='roles', operation='D')
    async def create_query(self, request):
        query = """INSERT INTO "Role"."Roles"("RoleId", "ParentRoleId", "FullName", "Status")
        VALUES ('{}',null, '{}', true);"""
        data = json.loads(request.body.decode('utf-8'))
        query = query.format(data['RoleId'], data['FullName'])
        await self.insert_query(query)
        return SuccessResponse().return_response_object()

    @DRequests.rest_api_call(['PUT'], is_authenticated=True, claim='roles', operation='U')
    async def update(self, request):
        await self.create_update_function(json.loads(request.body.decode('utf-8')))
        return SuccessResponse().return_response_object()

    @DRequests.rest_api_call(['POST'], is_authenticated=True, claim='roles',operation='D')
    async def delete(self, request):
        await self.delete_function(json.loads(request.body.decode('utf-8')))
        return SuccessResponse().return_response_object()

urlpatterns = [
    path('roles/getAll', RolesController.as_view()),
    path('roles/findBy', RolesController.as_view()),
    path('roles/create', RolesController.as_view()),
    path('roles/create_query', RolesController.as_view()),
    path('roles/update', RolesController.as_view()),
    path('roles/delete', RolesController.as_view()),
]
