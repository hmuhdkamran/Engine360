#
#   auther: H.Muhammad Kamran
#   email: hmuhdkamran@gmail.com
#   contact: +92 (313 / 333) 9112 845
#

from Api.BaseClass import *
from Models.models import Routes

DRequests = DecoratorHandler()

class RoutesController(BaseClass):

    @staticmethod
    def purse(obj):
        return {
    'RouteId': str(obj.RouteId),'RouteName': obj.RouteName,'DisplayName': obj.DisplayName,'Status': obj.Status
        }

    @sync_to_async
    def retrieve_objects(self, items):
        return [self.purse(obj) for obj in items]

    @sync_to_async
    def get_all_function(self):
        return Routes.objects.all()

    @sync_to_async
    def find_by_function(self, search_string):
        return Routes.objects.filter(RouteId__icontains=search_string)

    @sync_to_async
    def create_update_function(self, data):
        Routes.objects.update_or_create(
            RouteId=data['RouteId'], defaults=dict(RouteId=data['RouteId'],RouteName=data['RouteName'],DisplayName=data['DisplayName'],Status=data['Status']))

    @sync_to_async
    def delete_function(self, data):
        Routes.objects.filter(RouteId=data['RouteId']).delete()

    @DRequests.rest_api_call(['GET'], is_authenticated=True, claim='routes', operation='R')
    async def getAll(self, request):
        start_index, limit = self.get_pagination_params(request)
        items = await self.get_all_function()
        paginate_ = Paginate(items, self.purse, start_index, limit)
        items = await self.paginate_response(paginate_)
        return SuccessResponse(data=items).return_response_object()

    @DRequests.rest_api_call(['POST'], is_authenticated=True, claim='routes',operation='R')
    async def findBy(self, request):
        data = json.loads(request.body.decode('utf-8'))
        items = await self.find_by_function(data['parameter'])
        items = await self.retrieve_objects(items)
        return SuccessResponse(data=items).return_response_object()

    @DRequests.rest_api_call(['POST'], is_authenticated=True, claim='routes', operation='C')
    async def create(self, request):
        await self.create_update_function(json.loads(request.body.decode('utf-8')))
        return SuccessResponse().return_response_object()

    @DRequests.rest_api_call(['PUT'], is_authenticated=True, claim='routes', operation='U')
    async def update(self, request):
        await self.create_update_function(json.loads(request.body.decode('utf-8')))
        return SuccessResponse().return_response_object()

    @DRequests.rest_api_call(['POST'], is_authenticated=True, claim='routes',operation='D')
    async def delete(self, request):
        await self.delete_function(json.loads(request.body.decode('utf-8')))
        return SuccessResponse().return_response_object()

urlpatterns = [
    path('routes/getAll', RoutesController.as_view()),
    path('routes/findBy', RoutesController.as_view()),
    path('routes/create', RoutesController.as_view()),
    path('routes/update', RoutesController.as_view()),
    path('routes/delete', RoutesController.as_view()),
]