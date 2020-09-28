
from Api.BaseClass import *
from Models.models import Roles

class RolesController(BaseClass):
    def dispatch(self, request, *args, **kwargs):
        if (request.method.lower() == "get" and request.path.split('/')[-1] == 'getAll'):
            return self.get_all()
        elif (request.method.lower() == "post" and request.path.split('/')[-1] == 'findBy'):
            return self.find_by(request)
        elif (request.method.lower() == "post" and request.path.split('/')[-1] == 'create') or (request.method.lower() == "post" and request.path.split('/')[-1] == 'update'):
            return self.create(request)
        elif (request.method.lower() == "post" and request.path.split('/')[-1] == 'delete'):
            return self.delete(request)

        return super().dispatch(request, *args, **kwargs)

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

    async def get_all(self):
        items = await self.get_all_function()
        items = await self.retrieve_objects(items)
        return SuccessResponse(data=items).return_response_object()

    async def find_by(self, request):
        data = json.loads(request.body.decode('utf-8'))
        items = await self.find_by_function(data['parameter'])
        items = await self.retrieve_objects(items)
        return SuccessResponse(data=items).return_response_object()

    async def create(self, request):
        await self.create_function(json.loads(request.body.decode('utf-8')))
        return SuccessResponse().return_response_object()

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