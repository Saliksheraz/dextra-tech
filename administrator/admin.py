from django.contrib import admin
from .models import sensorData, Warehouse, weatherStationData, FreezerWarehouse, FreezerDevice, FreezersData

admin.site.register(FreezerWarehouse)
admin.site.register(FreezerDevice)
admin.site.register(FreezersData)
admin.site.register(Warehouse)
