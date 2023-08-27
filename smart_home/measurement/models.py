# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
from django.db import models

class Sensor(models.Model):
    """Датчик - на котором проводят измерения."""

    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Сенсор'
        verbose_name_plural = 'Сенсоры'

    def __str__(self):
        return self.name

class Measurement(models.Model):
    """Измерение температуры на объекте."""

    temperature = models.FloatField(verbose_name='Температура') 
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Показание'
        verbose_name_plural = 'Показания'
