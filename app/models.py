from django.db import models


class Weather(models.Model):
    city = models.CharField(max_length=30)
    temperature = models.FloatField()
    humidity = models.FloatField()
    speed = models.FloatField()
    pressure = models.FloatField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
