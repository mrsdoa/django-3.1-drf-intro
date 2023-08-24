# TODO: опишите необходимые сериализаторы

from rest_framework import serializers
from measurement.models import Sensor, Measurement

#если сериализатор полностью копирует модель, наследуемся от класса ModelSerializer
#указанные параметры в сериализаторе будут выводиться при ответе в обработчике
class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at'] 


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at'] #'__all__'


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']