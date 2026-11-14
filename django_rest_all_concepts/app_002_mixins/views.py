from django.shortcuts import render
from django.views import View
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView
from app_002_mixins.mixin import *
from app_002_mixins.models import *
import json
from django.http import HttpResponse
from django.core.serializers import serialize
from app_002_mixins.utils import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from app_002_mixins.forms import *

# Create your views here.
class jsonResponseView(jsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        context = {
            'name': 'Django Rest Framework',
            'framework': 'Django',
            'language': 'Python'
        }
        return self.render_to_json_response(context)

class infotest(View):
    def get(self, request, id, *args, **kwargs):
        d = testInfo.objects.get(id = id)
        data = {'name': d.name, 'phone': d.phone, 'address': d.address}
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')

class showinfoTestList(View):
    # def get(self, request, *args, **kwargs):
    #     data = testInfo.objects.get(id = kwargs['id'])
    #     json_data = serialize('json', [data])
    #     # if we want to serialize only specific fields, we can use the 'fields' argument
    #     # in the serialize function. For example:
    #     json_data = serialize('json', [data], fields=('name', 'phone', 'address'))
    #     return HttpResponse(json_data, content_type='application/json')
    
    def get(self, request, *args, **kwargs):
        data = testInfo.objects.all()
        json_data = serialize('json', data)
        updated_json_data = json.loads(json_data)
        new_data = []
        for item in updated_json_data:
            new_data.append({
                'name': item['fields']['name'],
                'phone': item['fields']['phone'],
                'address': item['fields']['address']
            })
        d = json.dumps(new_data)
        return HttpResponse(d, content_type='application/json')

@method_decorator(csrf_exempt, name='dispatch')
class showinfoTestListWithMixin(serializeMixin, View):
    def get(self, request, *args, **kwargs):
        data = testInfo.objects.all()
        json_data = self.serialize_data(data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        data = request.body
        if not is_json(data):
            return HttpResponse(json.dumps({'msg': 'Please send valid JSON data'}), content_type='application/json', status=400)
        json_data = json.dumps({'msg': 'Data received successfully'})
        return HttpResponse(json_data, content_type='application/json', status=200)

class showMixinData(ListModelMixin, GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# Submit the form data using the form.py file and save it to the database using the model.py file. Then return a JSON response with a success message.
@method_decorator(csrf_exempt, name='dispatch')
class testInfoFormView(serializeMixin, View):
    def get(self, request, *args, **kwargs):
        if 'id' not in kwargs:
            data = testInfo.objects.all()
        else:
            data = testInfo.objects.filter(id=kwargs['id'])
        json_data = self.serialize_data(data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        data = request.body
        if not is_json(data):
            return HttpResponse(json.dumps({'msg': 'Please send valid JSON data'}), content_type='application/json', status=400)
        infoData = json.loads(data)
        form = testInfoForm(infoData)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({'msg': 'Data saved successfully'}), content_type='application/json', status=200)
        elif form.errors:
            return HttpResponse(json.dumps({'msg': 'Invalid data', 'errors': form.errors}), content_type='application/json', status=400)
        else:
            return HttpResponse(json.dumps({'msg': 'Invalid data', 'errors': form.errors}), content_type='application/json', status=400)

    def put(self, request, *args, **kwargs):
        data = request.body
        if not is_json(data):
            return HttpResponse(json.dumps({'msg': 'Please send valid JSON data'}), content_type='application/json', status=400)
        infoData = json.loads(data)
        try:
            obj = testInfo.objects.get(id=infoData['id'])
        except testInfo.DoesNotExist:
            return HttpResponse(json.dumps({'msg': 'Object does not exist'}), content_type='application/json', status=404)
        form = testInfoForm(infoData, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({'msg': 'Data updated successfully'}), content_type='application/json', status=200)
        elif form.errors:
            return HttpResponse(json.dumps({'msg': 'Invalid data', 'errors': form.errors}), content_type='application/json', status=400)
        else:
            return HttpResponse(json.dumps({'msg': 'Invalid data', 'errors': form.errors}), content_type='application/json', status=400)

    def delete(self, request, *args, **kwargs):
        data = request.body
        if not is_json(data):
            return HttpResponse(json.dumps({'msg': 'Please send valid JSON data'}), content_type='application/json', status=400)
        infoData = json.loads(data)
        try:
            obj = testInfo.objects.get(id=infoData['id'])
        except testInfo.DoesNotExist:
            return HttpResponse(json.dumps({'msg': 'Object does not exist'}), content_type='application/json', status=404)
        itemDeleted = obj.delete()
        return HttpResponse(json.dumps({'msg': 'Data deleted successfully'}), content_type='application/json', status=200, headers={'X-Deleted-Count': itemDeleted[0]})