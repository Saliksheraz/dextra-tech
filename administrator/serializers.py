from rest_framework import serializers
from .models import sensorData


class sensorsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = sensorData
        exclude = ['id', 'device']
