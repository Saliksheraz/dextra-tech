from django import forms
from .models import FreezerWarehouse, FreezerDevice
from django.contrib.auth.models import User


class freezerWarehouseForm(forms.ModelForm):
    class Meta:
        model = FreezerWarehouse
        fields = "__all__"


class freezerDeviceForm(forms.ModelForm):
    class Meta:
        model = FreezerDevice
        fields = "__all__"
