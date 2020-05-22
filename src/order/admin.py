from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'quantity', 'total_price' )
    list_filter = ('status',)
    search_fields = ('id',)
    ordering = ('-id', )


admin.site.register(Order, OrderAdmin)
