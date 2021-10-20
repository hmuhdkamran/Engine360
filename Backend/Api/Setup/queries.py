#
#   auther: H.Muhammad Kamran
#   email: hmuhdkamran@gmail.com
#   contact: +92 (313 / 333) 9112 845
#

from Api.BaseClass import *
from Models.models import Queries

DRequests = DecoratorHandler()

class QueriesController(BaseClass):

    @staticmethod
    def purse(obj):
        return {
    'QueryId': obj.QueryId,'FullName': obj.FullName,'Description': obj.Description,'Status': obj.Status
        }

    @sync_to_async
    def retrieve_objects(self, items):
        return [self.purse(obj) for obj in items]

    @sync_to_async
    def get_all_function(self):
        return Queries.objects.all()

    @sync_to_async
    def find_by_function(self, search_string):
        return Queries.objects.filter(QueryId__icontains=search_string)

    @sync_to_async
    def create_update_function(self, data):
        Queries.objects.update_or_create(
            QueryId=data['QueryId'], defaults=dict(QueryId=data['QueryId'],FullName=data['FullName'],Description=data['Description'],Status=data['Status']))

    @sync_to_async
    def delete_function(self, data):
        Queries.objects.filter(QueryId=data['QueryId']).delete()

    @DRequests.rest_api_call(['GET'], is_authenticated=True, claim='queries', operation='R')
    async def getAll(self, request):
        start_index, limit = self.get_pagination_params(request)
        items = await self.get_all_function()
        paginate_ = Paginate(items, self.purse, start_index, limit)
        items = await self.paginate_response(paginate_)
        return SuccessResponse(data=items).return_response_object()

    @DRequests.rest_api_call(['POST'], is_authenticated=True, claim='queries',operation='R')
    async def findBy(self, request):
        data = json.loads(request.body.decode('utf-8'))
        items = await self.find_by_function(data['parameter'])
        items = await self.retrieve_objects(items)
        return SuccessResponse(data=items).return_response_object()

    @DRequests.rest_api_call(['POST'], is_authenticated=True, claim='queries', operation='C')
    async def create(self, request):
        await self.create_update_function(json.loads(request.body.decode('utf-8')))
        return SuccessResponse().return_response_object()

    @DRequests.rest_api_call(['PUT'], is_authenticated=True, claim='queries', operation='U')
    async def update(self, request):
        await self.create_update_function(json.loads(request.body.decode('utf-8')))
        return SuccessResponse().return_response_object()

    @DRequests.rest_api_call(['POST'], is_authenticated=True, claim='queries',operation='D')
    async def delete(self, request):
        await self.delete_function(json.loads(request.body.decode('utf-8')))
        return SuccessResponse().return_response_object()

urlpatterns = [
    path('queries/getAll', QueriesController.as_view()),
    path('queries/findBy', QueriesController.as_view()),
    path('queries/create', QueriesController.as_view()),
    path('queries/update', QueriesController.as_view()),
    path('queries/delete', QueriesController.as_view()),
]