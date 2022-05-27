from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from freezers.models import FreezersData, FreezerWarehouse, FreezerDevice


@login_required
def index(request):
    redirect("freezerWarehouse")
    for each in FreezerWarehouse.objects.all():
        each.warehouse.set([FreezerWarehouse.objects.first()])
        each.save()
    allData = FreezerWarehouse.objects.none()
    if request.user.is_superuser:
        allData = FreezerWarehouse.objects.all()
    context = {"allData": allData}
    return render(request, "administrator/index.html", context)




################### admin panel ##############################
@login_required
def adminPanel(request):
    allFreezerWarehouses = FreezerWarehouse.objects.all()
    allFreezerDevices = FreezerDevice.objects.all()
    allFreezersData = FreezersData.objects.all()

    context = {"allFreezerWarehouses": allFreezerWarehouses, "allFreezerDevices": allFreezerDevices, "allFreezersData": allFreezersData}
    return render(request, "administrator/adminPanel.html", context)
