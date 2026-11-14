from django.http import JsonResponse
from django.core.serializers import serialize
import json

class jsonResponseMixin(object):
    def render_to_json_response(self, context, **kwargs):
        return JsonResponse(context, **kwargs)

class serializeMixin(object):
    def serialize_data(self, data):
        json_data = serialize('json', data)
        updated_json_data = json.loads(json_data)
        new_data = []
        for item in updated_json_data:
            new_data.append({
                'name': item['fields']['name'],
                'phone': item['fields']['phone'],
                'address': item['fields']['address']
            })
        json_new_data = json.dumps(new_data)
        return json_new_data