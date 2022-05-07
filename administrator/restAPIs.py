from .models import FreezerDevice, sensorData, FreezersData
from .serializers import FreezerDataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.mail import EmailMessage
from django.conf import settings


@api_view(["GET", "POST"])
def freezerData(request, pk):
    if request.method == "GET":
        temp = request.GET.get("temp", None)
        isActive = request.GET.get("isActive", None)
        start_date = request.GET.get("start_date", None)
        end_date = request.GET.get("end_date", None)
        deviceObj = FreezerDevice.objects.get(id=pk)
        if temp:
            FreezersData.objects.create(temp=temp, isActive=isActive, device=deviceObj, warehouse=deviceObj.warehouse)
            if float(temp) > deviceObj.maxTempLimit:
                recipientsArray = deviceObj.warehouse.emailRecipents.split(',')
                if recipientsArray:
                    try:
                        email_msg = EmailMessage("Temp Exceeded", "Temp Exceeded the limit", settings.EMAIL_FROM, recipientsArray)
                        email_msg.send()
                        print("Email Sent")
                    except Exception as error:
                        print(error)
            return Response({"message": "Data Added Successfully!"}, status=status.HTTP_201_CREATED)
        allData = FreezersData.objects.filter(device_id=pk).order_by("-id")[:12]
        allData = reversed(allData)
        serializer = FreezerDataSerializer(allData, many=True)
        return Response(serializer.data)

    return Response({"message": "Hello, world!"})


class freezerDasdfsdfdta(APIView):
    def get(self, request, pk, format=None):
        allData = FreezersData.objects.filter(device_id=pk).order_by("-id")[:10]
        allData = reversed(allData)
        serializer = FreezerDataSerializer(allData, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FreezerDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
