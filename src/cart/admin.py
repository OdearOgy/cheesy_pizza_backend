from django.contrib import admin

from .models import *


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'state')
    ordering = ('-id', )


admin.site.register(Cart, CartAdmin)
