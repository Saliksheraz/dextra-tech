from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Compartment, Warehouse
from pymongo import MongoClient
from django.http import JsonResponse, QueryDict
import requests
import json


@login_required
def smartracks(request):
    allData = Warehouse.objects.all()
    context = {"allData": allData}
    return render(request, "smartracks/smartrack.html", context)


@login_required
def warehouse(request, pk):
    if request.method == "POST" and request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
        form_data = QueryDict(request.POST["serializedForm"].encode("ASCII"))
        url = "https://api.airliftgrocer.com/compartment/status"

        payload = json.dumps(
            {"warehouseId": warehouse.warehouseId,
                "rack": form_data["compartment"], "status": form_data["status"], "side": form_data["side"]}
        )
        headers = {"auth": "Groc3R@Sm@rtR@ck",
                   "Content-Type": "application/json"}

        response = requests.request("PUT", url, headers=headers, data=payload)

        if response.status_code == 200:
            return JsonResponse({"message": "Updated Successfully"})
        else:
            return JsonResponse({"message": "Request Failed"})
    allCompartments = Compartment.objects.filter(warehouse_id=pk)
    context = {"allCompartments": allCompartments}
    return render(request, "smartracks/warehouse.html", context)
