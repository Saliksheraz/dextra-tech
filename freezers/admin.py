from django.contrib import admin
from .models import FreezerWarehouse, FreezerDevice, FreezersData

admin.site.register(FreezerWarehouse)
admin.site.register(FreezerDevice)
admin.site.register(FreezersData)
