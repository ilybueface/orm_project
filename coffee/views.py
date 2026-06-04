from django.contrib.sessions import serializers
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from coffee.serilizator import Drinkserializers, Categoryserializers
from .models import Drink, Category

@api_view(['GET', 'POST'])
def drink_list(request):
    drinks = Drink.objects.all()
    drk = Drinkserializers(drinks, many=True)
    if request.method == 'POST':
        serializer = Drinkserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(drk.data)


@api_view(['GET'])
def category(request):
    ctga = Category.objects.all()
    ctg = Categoryserializers(ctga, many=True)
    return Response(ctg.data)


@api_view(['GET'])
def drink_detail(request, pk):
    item = Drink.objects.get(id=pk)
    itemser = Drinkserializers(item)
    return Response(itemser.data)