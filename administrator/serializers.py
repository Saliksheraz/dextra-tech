from rest_framework import serializers
from .models import sensorData, FreezersData


class FreezerDataSerializer(serializers.ModelSerializer):
    datetime = serializers.SerializerMethodField()
    change = serializers.SerializerMethodField()

    class Meta:
        model = FreezersData
        exclude = ["id", "device", "warehouse"]

    def get_datetime(self, obj):
        return obj.datetime.strftime("%m/%d/%Y, %H:%M:%S")

    def get_change(self, obj):
        try:
            secondLastObj = FreezersData.objects.filter(device=obj.device).order_by('-id')[1]
            change = obj.temp - secondLastObj.temp
            return change
        except:
            return 0
        