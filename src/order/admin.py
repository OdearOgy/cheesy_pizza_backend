from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_total_price', 'get_delivery_fee', 'status' )
    list_filter = ('status',)
    search_fields = ('id',)
    ordering = ('-id', )

admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
