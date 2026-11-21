from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app_004_modelSerialization.models import *
from app_004_modelSerialization.serializers import *
# Create your views here.
class informationView(APIView):
    def get(self, request):
        id = request.query_params.get('id', None)
        try:
            if id is not None:
                data = information.objects.get(id=id)
                serializer = informationSerializer(data)
            else:
                data = information.objects.all()
                serializer = informationSerializer(data, many=True)

            if serializer.data:
                return Response({'msg': 'Data is available', 'data': serializer.data})
            else:
                return Response({'msg': 'data is not present'})
        except information.DoesNotExist:
            return Response({'msg': 'Record not found'}, status=404)

        except Exception as e:
            return Response({'msg': 'Error while processing GET request','error': str(e)}, status=500)

    def post(self, request):
        serializer = informationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Information data is saved'})
        return Response(serializer.errors, status=400)
        

