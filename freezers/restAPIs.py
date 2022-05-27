from .models import FreezerDevice, FreezersData
from .serializers import FreezerDataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.mail import EmailMessage
from django.conf import settings
from datetime import datetime, timezone


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
            if float(temp) > deviceObj.warehouse.maxTempLimit:
                recipientsArray = deviceObj.warehouse.emailRecipents.split(",")
                if recipientsArray:
                    try:
                        email_msg = EmailMessage("Temp Exceeded", "Temp Exceeded the limit", settings.EMAIL_FROM, recipientsArray)
                        email_msg.send()
                        print("Email Sent")
                    except Exception as error:
                        print(error)
            return Response({"message": "Data Added Successfully!"}, status=status.HTTP_201_CREATED)
        allData = FreezersData.objects.filter(device_id=pk)
        if allData:
            lastData = allData.last()
            now = datetime.now(timezone.utc)
            lastUpdated = (now - lastData.datetime).total_seconds()
            if lastUpdated > 100:
                deviceObj.isActive = False
            else:
                deviceObj.isActive = True
            deviceObj.save()
        allData = reversed(allData.order_by("-id")[:15])
        serializer = FreezerDataSerializer(allData, many=True)
        return Response(serializer.data)

    return Response({"message": "Hello, world!"})
