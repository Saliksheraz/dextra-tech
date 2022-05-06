from django.contrib import admin
from .models import sensorData, Warehouse, weatherStationData

admin.site.register(sensorData)
admin.site.register(weatherStationData)
admin.site.register(Warehouse)
