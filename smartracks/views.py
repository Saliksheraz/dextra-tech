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
    allCompartments = Compartment.objects.filter(warehouse_id=pk)
    context = {"allCompartments": allCompartments}
    return render(request, "smartracks/warehouse.html", context)
