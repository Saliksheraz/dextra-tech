from pickle import TRUE
from django.db import models


class Warehouse(models.Model):
    warehouseId = models.CharField(max_length=200, null=True)
    serverState = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.warehouseId


class Compartment(models.Model):
    compartment = models.CharField(max_length=10, null=True)
    warehouse = models.ForeignKey(
        Warehouse, on_delete=models.CASCADE, null=True)
    boxstate = models.CharField(max_length=10, null=True)
    code = models.CharField(max_length=10, null=True)
    livestatedisplay = models.CharField(max_length=10, null=True)
    livestaterelay = models.CharField(max_length=10, null=True)
    livestatefeedback = models.CharField(max_length=10, null=True)
    smartenable = models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return self.compartment
