from rest_framework import serializers

from item.models import Item
from order.models import *


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    class Meta:
        model = OrderItem
        fields = '__all__'
        
        
class OrderSerializer(serializers.Serializer):  
  id = serializers.IntegerField()
  slug = serializers.SlugField()
  creation_date = serializers.DateTimeField()
  update_date = serializers.DateTimeField()
  total_price = serializers.DecimalField(max_digits=7, decimal_places=2, default=0,)
  delivery_fee = serializers.DecimalField(max_digits=7, decimal_places=2, default=0,)
  items = OrderItemSerializer(many=True, read_only=True)
