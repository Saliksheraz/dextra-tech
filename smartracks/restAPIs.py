from doctest import COMPARISON_FLAGS
import re
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Warehouse, Compartment


@api_view(["POST"])
def warehouseData(request, pk):
    warehouseObj = Warehouse.objects.filter(warehouseId=pk)
    print(warehouseObj)
    if warehouseObj:
        warehouseObj = warehouseObj[0]
    else:
        warehouseObj = Warehouse.objects.create(warehouseId=pk)
    allData = request.data
    for each in allData:
        compartmentObj = Compartment.objects.filter(
            compartment=each["compartment"])
        if compartmentObj:
            compartmentObj = compartmentObj[0]
            compartmentObj.boxstate = each["boxstate"]
            compartmentObj.code = each["code"]
            compartmentObj.livestatedisplay = each["livestatedisplay"]
            compartmentObj.livestaterelay = each["livestaterelay"]
            compartmentObj.livestatefeedback = each["livestatefeedback"]
            compartmentObj.smartenable = each["smartenable"]
            compartmentObj.save()
        else:
            Compartment.objects.create(warehouse=warehouseObj, compartment=each["compartment"], boxstate=each["boxstate"], code=each["code"], livestatedisplay=each["livestatedisplay"],
                                       livestaterelay=each["livestaterelay"], livestatefeedback=each["livestatefeedback"], smartenable=each["smartenable"])
        # print(each
    return Response({"message": "Success!"})
