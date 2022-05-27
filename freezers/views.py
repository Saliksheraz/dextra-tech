from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import FreezersData, FreezerWarehouse, FreezerDevice
from .forms import freezerWarehouseForm, freezerDeviceForm
from django.contrib import messages


@login_required
def freezerWarehouse(request):
    if request.method == "POST":
        form = freezerWarehouseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"Freezer Warehouse Added Successfully !!!")
            return redirect("index")
        else:
            print(form.errors)
            messages.success(request, form.errors)
    form = freezerWarehouseForm()
    allData = FreezerWarehouse.objects.all()
    context = {"form": form, "allData": allData}
    return render(request, "administrator/freezerWarehouse.html", context)


@login_required
def freezerDevice(request, pk):
    if request.method == "POST":
        form = freezerDeviceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Freezer Device Added Successfully !!!")
            return redirect("index")
        else:
            print(form.errors)
            messages.success(request, form.errors)
    form = freezerDeviceForm()
    allData = FreezerDevice.objects.filter(warehouse_id=pk)
    for each in allData:
        data = FreezersData.objects.filter(device_id=each.id).last()
        if data:
            each.temp = data.temp
            each.datetime = data.datetime
    context = {"form": form, "allData": allData}
    return render(request, "administrator/freezerDevice.html", context)
