from django.db import models


class Warehouse(models.Model):
    name = models.CharField(max_length=200)
    weight = models.FloatField()
    Time_duration = models.IntegerField()


