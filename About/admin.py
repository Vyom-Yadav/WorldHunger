from django.contrib import admin
from . models import Warehouse_stock


class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'Time_duration')


admin.site.register(Warehouse_stock, StockAdmin)

