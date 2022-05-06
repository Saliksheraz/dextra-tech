import datetime
import datedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import sensorData, Warehouse, weatherStationData
import random
from .forms import warehouseForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import User


@login_required
def index(request):
    allData = Warehouse.objects.none()
    if request.user.is_superuser:
        allData = Warehouse.objects.all()
    context = {'allData': allData}
    return render(request, 'administrator/index.html', context)


@login_required
def warehouse(request):
    if request.method == 'POST':
        form = warehouseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Warehouse Added Successfully !!!')
            return redirect('index')
        else:
            print(form.errors)
    form = warehouseForm()
    context = {'form': form}
    return render(request, 'administrator/warehouse.html', context)

