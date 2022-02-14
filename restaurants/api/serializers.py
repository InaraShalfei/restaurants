from rest_framework import serializers

from .models import Restaurant, Pizza


class RestaurantSerializer(serializers.ModelSerializer):
    model = Restaurant
    fields = '__all__'


class PizzaSerializer(serializers.ModelSerializer):
    model = Pizza
    fields = '__all__'
