from statistics import mode
from django.db import models
from django.contrib.auth.models import User


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


class Warehouse(models.Model):
    name = models.CharField(max_length=200, null=True)
    warehouseId = models.CharField(max_length=200, null=True)
    picture = models.ImageField(null=True, blank=True)
    

    def __str__(self):
        return self.name


class SmartRack(models.Model):
    # warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    createdAt = models.DateField(null=True, auto_now=True)
    picture = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    latitude = models.CharField(max_length=50, blank=True)
    longitude = models.CharField(max_length=50, blank=True)
    type_choices = (
        ("Temperature+Humidity", "Temperature+Humidity"),
        ("NPK+Temperature+Humidity", "NPK+Temperature+Humidity"),
        ("Hydroponics", "Hydroponics"),
        ("Custom", "Custom"),
    )
    type = models.CharField(max_length=100, choices=type_choices, default="Dormant")
    warehouse = models.ManyToManyField(Warehouse, null=True, verbose_name="warehouse")

    def __str__(self):
        return self.name


class sensorData(models.Model):
    # device = models.ForeignKey(device, on_delete=models.CASCADE, null=True, blank=True)
    srNumber = models.CharField(max_length=200, null=True)
    timeStamp = models.DateTimeField(null=True)
    temperature = models.IntegerField(null=True)
    battery = models.IntegerField(null=True, blank=True)
    soilMoisture = models.CharField(max_length=200, null=True)
    humidity = models.IntegerField(null=True)
    ppm = models.IntegerField(null=True)
    ph = models.IntegerField(null=True)
    waterTemp = models.CharField(max_length=200, null=True)
    energyConsumption = models.CharField(max_length=200, null=True)
    waterLevel = models.CharField(max_length=200, null=True)
    n = models.CharField(max_length=200, null=True)
    p = models.CharField(max_length=200, null=True)
    k = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.srNumber


class weatherStationData(models.Model):
    # device = models.ForeignKey(device, on_delete=models.CASCADE, null=True, blank=True)
    srNumber = models.CharField(max_length=200, null=True)
    timeStamp = models.DateTimeField(null=True)
    temperature = models.IntegerField(null=True)
    pressure = models.CharField(max_length=20, null=True)
    local_temperature = models.CharField(max_length=20, null=True)
    local_humidity = models.CharField(max_length=20, null=True)
    local_pressure = models.CharField(max_length=20, null=True)
    solar_radiation = models.CharField(max_length=20, null=True)
    sun_rise = models.CharField(max_length=20, null=True)
    sun_set = models.CharField(max_length=20, null=True)
    sun_duration = models.CharField(max_length=20, null=True)
    wind_direction = models.CharField(max_length=20, null=True, blank=True)
    wind_speed = models.CharField(max_length=20, null=True)
    air_quality = models.CharField(max_length=20, null=True)
    battery = models.CharField(max_length=20, null=True)
    humidity = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.srNumber
