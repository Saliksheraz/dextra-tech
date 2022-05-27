from django.db import models

class Warehouse(models.Model):
    warehouseId = models.CharField(max_length=200, null=True)    

    def __str__(self):
        return self.warehouseId
