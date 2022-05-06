from dataclasses import field
from django import forms
from .models import Warehouse
from django.contrib.auth.models import User


class warehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'

