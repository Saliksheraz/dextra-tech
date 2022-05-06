from .models import sensorData
from .serializers import sensorsDataSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import sensorsDataSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        snippets = sensorData.objects.all()
        serializer = sensorsDataSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = sensorsDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class sensorsDataView(APIView):
    def get(self, request, pk, items, format=None):
        allData = sensorData.objects.filter(
            device_id=pk).order_by('-id')[:items]
        allData = reversed(allData)
        serializer = sensorsDataSerializer(allData, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = sensorsDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
