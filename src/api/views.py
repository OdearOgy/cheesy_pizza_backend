from rest_framework.generics import ListAPIView, RetrieveAPIView
from item.models import Item
from .serializers import ItemSerializer

class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'slug'