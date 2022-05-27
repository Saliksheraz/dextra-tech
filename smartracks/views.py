from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Warehouse
from pymongo import MongoClient
import requests


@login_required
def smartracks(request):
    allData = Warehouse.objects.all()
    context = {"allData":allData}
    return render(request, "smartracks/smartrack.html", context)


@login_required
def warehouse(request, pk):
    warehouse = Warehouse.objects.get(id=pk)
    client = MongoClient("mongodb+srv://Salik:JFAVPkCgW8mtXRN@cluster0.p1m4g.mongodb.net/NodesData?retryWrites=true&w=majority")
    mongoDatabase = client[f"warehouse{warehouse.warehouseId}"]
    collection = mongoDatabase["compartmentsinfos"]

    url = "https://api.airliftgrocer.com/v2/orders/packed/compartments?warehouse=" + warehouse.warehouseId
    headers = {"auth": "Groc3R@Sm@rtR@ck"}
    cloudData = requests.get(url, headers=headers)
    if cloudData.text:
        cloudData = cloudData.json()
        # for each in cloudData:
        #     rtObj = collection.find_one({"compartment": each["compartment"]})
        #     each["status"] = rtObj["status"]
        #     each["rtBoxstate"] = rtObj["boxstate"]
        #     each["rtCode"] = rtObj["code"]
        context = {"cloudData": cloudData}
        return render(request, "smartracks/warehouse.html", context)
    context = {}
    return render(request, "smartracks/warehouse.html", context)
