from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Warehouse
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
    warehouse = Warehouse.objects.get(id=pk)
    if request.method == "POST" and request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
        form_data = QueryDict(request.POST["serializedForm"].encode("ASCII"))
        url = "https://api.airliftgrocer.com/compartment/status"
    
        payload = json.dumps(
            {"warehouseId": warehouse.warehouseId, "rack": form_data["compartment"], "status": form_data["status"], "side": form_data["side"]}
        )
        headers = {"auth": "Groc3R@Sm@rtR@ck", "Content-Type": "application/json"}

        response = requests.request("PUT", url, headers=headers, data=payload)

        if response.status_code == 200:
            return JsonResponse({"message":"Updated Successfully"})
        else:
            return JsonResponse({"message":"Request Failed"})
    try:
        client = MongoClient("mongodb+srv://Salik:JFAVPkCgW8mtXRN@cluster0.p1m4g.mongodb.net/NodesData?retryWrites=true&w=majority")
        mongoDatabase = client[f"warehouse{warehouse.warehouseId}"]
        collection = mongoDatabase["compartmentsinfos"]
        cloudData = collection.find()
        context = {"cloudData": cloudData}
    except:
        context = {}
    return render(request, "smartracks/warehouse.html", context)
