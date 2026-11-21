from django.shortcuts import render
from django.views.generic import View
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from app_003_serialization.models import *
from app_003_serialization.serializers import *
import io

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class detailView(View):
    # GET: Retrieve record
    def get(self, request, *args, **kwargs):
        # json_data = request.body
        # stream = io.BytesIO(json_data)
        # data = JSONParser().parse(stream)
        # id  = data.get('id', None)
        # if id is not None:
        #     data = detail.objects.get(id=id)
        #     serializer = detailSerializer(data)
        #     json_data = JSONRenderer().render(serializer.data)
        # else:
        #     data = detail.objects.all()
        #     serializer = detailSerializer(data, many=True)
        #     json_data = JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data, content_type='application/json')
        id = request.GET.get('id', None)
        if id is not None:
            try:
                data = detail.objects.get(id=id)
                serializer = detailSerializer(data)
            except detail.DoesNotExist:
                msg = {'error': 'Record not found'}
                json_data = JSONRenderer().render(msg)
                return HttpResponse(json_data, content_type='application/json', status=404)
        else:
            data = detail.objects.all()
            serializer = detailSerializer(data, many=True)
        
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    # POST: Create record
    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        serializer = detailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg': 'Record successfully created'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type = 'application/json', status=201)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json', status=400)

    # PUT: Update record
    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get('id', None)
        if id is None:
            msg = {'error': 'ID is required for updating a record'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json', status=400)
        try:
            detail_data = detail.objects.get(id=id)
        except detail.DoesNotExist:
            msg = {'error': 'Record not found'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json', status=404)
        
        serializer = detailSerializer(detail_data, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg': 'Record successfully updated'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')

    # DELETE: Delete record
    def delete(self, request, *args, **kwargs):
        id = request.GET.get('id', None)
        if id is None:
            msg = {'error': 'ID is required for deleting a record'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json', status=400)
        try:
            data = detail.objects.get(id=id)
            data.delete()
            msg = {'msg': 'Record successfully deleted'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse( json_data, content_type='application/json')
        except detail.DoesNotExist:
            msg = {'error': 'Record not found'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json', status=404)




        