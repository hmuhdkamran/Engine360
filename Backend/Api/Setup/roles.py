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
                ParentRoleId=data['ParentRoleId'],
                FullName=data['FullName'],
                Status=data['Status']))

    @sync_to_async
    def delete_function(self, data):
        Roles.objects.filter(RoleId=data['RoleId']).delete()

    @DRequests.rest_api_call(['GET'], is_authenticated=True, claim='setup', operation='R')
    async def getAll(self, request):
        start_index, limit = self.get_pagination_params(request)
        items = await self.get_all_function()
        paginate_ = Paginate(items, self.purse, start_index, limit)
        items = await self.paginate_response(paginate_)
        # items = await self.retrieve_objects(items)
        return SuccessResponse(data=items).return_response_object()

    @DRequests.rest_api_call(['POST'], is_authenticated=True, claim='setup',operation='R')
    async def findBy(self, request):
        data = json.loads(request.body.decode('utf-8'))
        items = await self.find_by_function(data['parameter'])
        items = await self.retrieve_objects(items)
        return SuccessResponse(data=items).return_response_object()

    @DRequests.rest_api_call(['POST'], is_authenticated=True, claim='setup', operation='C')
    async def create(self, request):
        await self.create_update_function(json.loads(request.body.decode('utf-8')))
        return SuccessResponse().return_response_object()

    @DRequests.rest_api_call(['POST'], is_authenticated=True, claim='setup', operation='U')
    async def update(self, request):
        await self.create_update_function(json.loads(request.body.decode('utf-8')))
        return SuccessResponse().return_response_object()

    @DRequests.rest_api_call(['POST'], is_authenticated=True, claim='setup',operation='D')
    async def delete(self, request):
        await self.delete_function(json.loads(request.body.decode('utf-8')))
        return SuccessResponse().return_response_object()


urlpatterns = [
    path('setup/getAll', RolesController.as_view()),
    path('setup/findBy', RolesController.as_view()),
    path('setup/create', RolesController.as_view()),
    path('setup/update', RolesController.as_view()),
    path('setup/delete', RolesController.as_view()),
]
