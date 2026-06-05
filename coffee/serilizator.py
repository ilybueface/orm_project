from .models import Drink, Category, Order
from rest_framework import serializers


class Drinkserializers(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = [
            'id',
            'name',
            'price',
            'category'
        ]


class Categoryserializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name'
        ]


class Orderserializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'date',
            'drink'
        ]
