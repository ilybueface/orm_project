from rest_framework import viewsets
from coffee.serilizator import Drinkserializers, Categoryserializers, Orderserializers
from .models import Drink, Category, Order
from .permissions import IsAdminOrReadOnly
from .filter import DrinkFilter
from .pagination import CustomMetaPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = Drinkserializers
    filterset_fields = ['category__id', 'price']
    filterset_class = DrinkFilter
    pagination_class = CustomMetaPagination
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=False, methods=['get'])
    def cheap_drinks(self, request):
        drinks = Drink.objects.filter(price__lt=300)
        drks = Drinkserializers(drinks, many=True)
        return Response(drks.data)

    @action(detail=False, methods=['get'])
    def low_price(self, request):
        drinks = Drink.objects.all().order_by('price')
        drks = Drinkserializers(drinks, many=True)
        return Response(drks.data)

    @action(detail=False, methods=['get'], url_path='most-expensive')
    def expensive_drink(self, request):
        drink = Drink.objects.all().order_by('-price').first()
        drk = Drinkserializers(drink)
        return Response(drk.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Categoryserializers
    permission_classes = [AllowAny]

    @action(detail=True, methods=['get'])
    def all_drinks(self, request, pk=None):
        ctg_drinks = Drink.objects.filter(category=pk)
        serializer = Drinkserializers(ctg_drinks, many=True)
        return Response(serializer.data)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = Orderserializers
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['GET'])
    def today_orders(self, request, pk=None):
        order = self.get_object()
        serializer = Orderserializers(order)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def all_orders(self, request):
        order = Order.objects.count()
        return Response({'count': order})
