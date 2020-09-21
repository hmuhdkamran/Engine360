import json
import uuid

from asgiref.sync import sync_to_async
from django.db import connection

from Api.BaseClass import BaseClass
from Handler.RequestHandler import DecoratorHandler, SuccessResponse
from Helper.Pagination import Paginate
from Models.models import Business

DRequests = DecoratorHandler()


class BusinessClass(BaseClass):

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() == "get" and request.path.split('/')[-1] == 'get_business':
            return self.get_business(request)
        elif request.method.lower() == "post" and request.path.split('/')[-1] == 'post_business':
            return self.post_business(request)

        return super().dispatch(request, *args, **kwargs)

    @sync_to_async
    def create_business_object(self, data):
        return Business.objects.update_or_create(BusinessId=uuid.uuid1(), Abbreviation=data['Abbreviation'],
                                                 FullName=data['FullName'], Address=data['Address'])

    @sync_to_async
    def update_business_object(self, data):
        Business.objects.filter(BusinessId=data['BusinessId']).update(Abbreviation=data['Abbreviation'],
                                                                      FullName=data['FullName'],
                                                                      Address=data['Address'])

    @sync_to_async
    def delete_business_object(self, data):
        Business.objects.filter(BusinessId=data['BusinessId']).delete()

    @sync_to_async
    def get_all_business_object(self):
        return Business.objects.all()

    @sync_to_async
    def find_by_business_object(self, find_by):
        with connection.cursor() as cursor:
            query = """Select BusinessId, Abbreviation, FullName, Address from "Setup"."Business" where {}"""
            query = query.format(find_by)
            cursor.execute(query)
            col_desc = cursor.description
            column_names = [col[0] for col in col_desc]
            rows = cursor.fetchall()
            return [dict(zip(column_names, row)) for row in rows]

    @sync_to_async
    def find_by_business_object_orm(self, search_string):
        return Business.objects.filter(Abbreviation__icontains=search_string, FullName__icontains=search_string)

    @staticmethod
    def extract_object(obj):
        return {
            'BusinessId': str(obj.BusinessId),
            'Abbreviation': obj.Abbreviation,
            'FullName': obj.FullName,
            'Address': obj.Address
        }

    @sync_to_async
    def paginate_return(self, paginate_):
        return paginate_.paginate()

    async def get_business(self, request):
        start_index = request.GET.get('start_index', 0)
        limit = request.GET.get('limit', 10)
        limit = int(limit)
        start_index = int(start_index)
        business_obj = await self.get_all_business_object()
        paginate_ = Paginate(business_obj, self.extract_object, start_index, limit)
        items = await self.paginate_return(paginate_)
        return SuccessResponse(data=items).return_response_object()

    async def post_business(self, request):
        data = json.loads(request.body.decode('utf-8'))
        data['Address'] = data['Address'] if 'Address' in data else ''
        await self.create_business_object(data)
        return SuccessResponse().return_response_object()
