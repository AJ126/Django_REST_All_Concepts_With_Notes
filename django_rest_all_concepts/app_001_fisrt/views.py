from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic import View
# Create your views here.

@api_view(['GET'])
def first_api(request):
    return Response({"message": "Hello, this is the first API!"})

@api_view(['GET'])
def customer_list(request):
    customers = [{"id": 1, "name": "Shiv"}, {"id": 2, "name": "Parvati"}]
    return Response(customers)

class CustomerListView(View):
    def get(self, request):
        customers = [{"id": 1, "name": "Shiv"}, {"id": 2, "name": "Parvati"}]
        return JsonResponse(customers, safe=False)