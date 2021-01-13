from django.db import models


class Warehouse_stock(models.Model):
    name = models.CharField(max_length=200)
    weight = models.FloatField()
    Time_duration = models.IntegerField()


