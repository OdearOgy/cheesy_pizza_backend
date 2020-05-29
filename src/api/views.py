from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

from django.shortcuts import get_object_or_404
from decimal import Decimal

from item.models import Item
from order.models import *

from .serializers import ItemSerializer, OrderSerializer

class ItemViewSet(ReadOnlyModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    
    # retrieve single order using slug instead of the id
    def retrieve(self, request, pk=None):
        queryset = self.queryset
        order = get_object_or_404(queryset, slug=pk)
        serializer = ItemSerializer(order)
        
        return Response(serializer.data)
    
    

class OrderViewSet(ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    
    # retrieve single order using slug instead of the id
    def retrieve(self, request, pk=None):
        queryset = self.queryset
        order = get_object_or_404(queryset, slug=pk)
        serializer = OrderSerializer(order)
        
        return Response(serializer.data)



# Change the permissions to IsAuthenticated 
# and add the user profiles
# add this as a create method for the
# OrderViewSet

@api_view(['POST'])
@permission_classes((AllowAny, ))
def makeOrder(request):
    resp = {
      'type': 'error',
      'response': 'Error',
    }
    try: 
      prices = request.data['prices']
      items = []
      for item in request.data['items']:
        ord = OrderItem()
        ord.item = Item.objects.get(slug=item['slug'])
        ord.quantity = item['quantity']
        ord.clean_fields()
        ord.save()
        items.append(ord)      

      order = Order()
      order.total_price = Decimal(str(prices['total']))
      order.delivery_fee = Decimal(str(prices['delivery']))
      order.clean_fields()
      order.save()
      order.items.set(items)
      order.save()
          
    except Exception as e:
      resp['response'] = f'{e}'
      return Response(resp)
    
    
    resp = {
      'type': 'ok',   
      'response': 'Order Created',
      'order_slug': f'{order.slug}'
    }  
    
    return Response(resp)

    

    
    
    
    


