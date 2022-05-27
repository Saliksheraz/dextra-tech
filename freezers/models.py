from django.db import models

class FreezerWarehouse(models.Model):
    name = models.CharField(max_length=200, null=True)
    warehouseId = models.IntegerField(null=True)
    location = models.CharField(max_length=200, null=True)
    maxTempLimit = models.FloatField(null=True)
    picture = models.ImageField(null=True, blank=True)
    emailRecipents = models.CharField(max_length=200, null=True)
    smsRecipents = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name


class FreezerDevice(models.Model):
    name = models.CharField(max_length=200, null=True)
    deviceId = models.IntegerField(null=True)
    isActive = models.BooleanField(default=False)
    warehouse = models.ForeignKey(FreezerWarehouse, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class FreezersData(models.Model):
    temp = models.FloatField(null=True)
    datetime = models.DateTimeField(auto_now=True)
    device = models.ForeignKey(FreezerDevice, on_delete=models.CASCADE, null=True)
    warehouse = models.ForeignKey(FreezerWarehouse, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.temp)