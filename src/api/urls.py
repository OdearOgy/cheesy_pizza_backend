from rest_framework.routers import DefaultRouter 
from django.urls import path
from .views import *

router = DefaultRouter()

router.register(r'items', ItemViewSet, basename='item')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = router.urls

urlpatterns += [
    path('order/create/', makeOrder, name='make_order'),
]