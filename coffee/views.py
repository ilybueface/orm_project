from django.contrib.sessions import serializers
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from coffee.serilizator import Drinkserializers, Categoryserializers, Orderserializers
from .models import Drink, Category, Order

@api_view(['GET', 'POST'])
def drink_list(request):
    drinks = Drink.objects.all()
    drk = Drinkserializers(drinks, many=True)
    if request.method == 'POST':
        serializer = Drinkserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(drk.data)


@api_view(['GET'])
def category(request):
    ctga = Category.objects.all()
    ctg = Categoryserializers(ctga, many=True)
    return Response(ctg.data)


@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, pk):
    item = get_object_or_404(Drink, id=pk)
    itemser = Drinkserializers(item)
    if request.method == 'PUT':
        serializer = Drinkserializers(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    if request.method == 'DELETE':
        item.delete()
        return Response('', status=status.HTTP_204_NO_CONTENT)
    return Response(itemser.data)


@api_view(['GET', 'POST'])
def order_list(request):
    order = Order.objects.all()
    ord = Orderserializers(order, many=True)
    if request.method == 'POST':
        serializer = Orderserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(ord.data)


@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, pk):
    order_det = get_object_or_404(Order, id=pk)
    orddet = Orderserializers(order_det)
    if request.method == 'PUT':
        serializers = Orderserializers(order_det, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
    if request.method == 'DELETE':
        order_det.delete()
        return Response('', status=status.HTTP_204_NO_CONTENT)
    return Response(order_det.data)

