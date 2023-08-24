# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, SensorsSerializer, MeasurementSerializer, \
    MeasurementDetailSerializer

# по умолчанию listapiview реализует get, но не реализует поведения для post запросов, поэтому задаём его отдельно
# 1 - Создать датчик. Указываются название и описание датчика.
class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer

    def post(self, request):
        Sensor.objects.create(
            name=request.POST.get("name"),
            description=request.POST.get("description")
        )
        return Response({'status': 'OK'})

#инфо по одному только объекту реализуется с помощью класса RetrieveAPIView 
# 2 - Изменить датчик. Указываются название и описание.
class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk)
        sensor.description = request.data["description"]
        sensor.save()
        return Response({'status': 'OK'})

# 3 -Добавить измерение. Указываются ID датчика и температура.
# 4 - Получить список датчиков. Выдаётся список с краткой информацией по датчикам: ID, название и описание.
class MeasurementsView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementDetailSerializer

    def post(self, request):
        Measurement.objects.create(
            sensor_id=request.POST.get("sensor"),
            temperature=request.POST.get("temperature")
        )
        return Response({'status': 'OK'})