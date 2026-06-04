from .models import Drink, Category
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
