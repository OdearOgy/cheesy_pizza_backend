from django.contrib import admin

# Register your models here.

from .models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price',)
    search_fields = ('id', 'name')
    ordering = ('-id', )


admin.site.register(Item, ItemAdmin)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity',)
    search_fields = ('id', 'name')
    ordering = ('-id', )


admin.site.register(Ingredient, IngredientAdmin)
