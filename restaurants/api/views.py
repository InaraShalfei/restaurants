from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import Pizza, Restaurant
from .serializers import PizzaSerializer, RestaurantSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'address')


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('name', 'restaurant')
    search_fields = ('^name', '^cheese', '^pastry')
