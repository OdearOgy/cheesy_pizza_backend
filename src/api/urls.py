from django.urls import path

from .views import ItemListView, ItemDetailView


urlpatterns = [
    path('items/', ItemListView.as_view()),
    path('items/<slug>', ItemDetailView.as_view())
]