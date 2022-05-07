from dataclasses import field
from django import forms
from .models import Warehouse, FreezerWarehouse, FreezerDevice
from django.contrib.auth.models import User


class freezerWarehouseForm(forms.ModelForm):
    class Meta:
        model = FreezerWarehouse
        fields = "__all__"


class freezerDeviceForm(forms.ModelForm):
    class Meta:
        model = FreezerDevice
        fields = "__all__"


class warehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = "__all__"
