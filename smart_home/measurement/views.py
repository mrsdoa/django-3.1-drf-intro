# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response

from measurement.models import Sensor #Measurement
from measurement.serializers import MeasurementSerializer, SensorDetailSerializer

# 1 - Создать датчик. Указываются название и описание датчика.
# 4 - Получить список датчиков. Выдаётся список с краткой информацией по датчикам: ID, название и описание.
class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def get_queryset(self):
        queryset = Sensor.objects.all()
        return queryset # возвращает тоже самое super().get_queryset() ?

    def perform_create(self, serializer):
        serializer.save()

#инфо по одному только объекту реализуется с помощью класса RetrieveAPIView 
# 2 - Изменить датчик. Указываются название и описание.
class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def get_queryset(self):
        queryset = Sensor.objects.all()
        return queryset #super().get_queryset() ?
    
    def perform_update(self, serializer):
        serializer.save()
    
# 3 -Добавить измерение. Указываются ID датчика и температура.
class MeasurementsView(CreateAPIView):
    # queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def perform_update(self, serializer):
        serializer.save()
