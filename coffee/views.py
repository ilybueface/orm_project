from coffee.serilizator import (
    Drinkserializers,
    Categoryserializers,
    Orderserializers,
    Reviewserializers,
    Promotionserializers,
    Favoriteserializer,
    Ingredientsserializer,
)
from rest_framework.filters import SearchFilter
from rest_framework import viewsets
from .models import (
    Drink,
    Category,
    Order,
    Review,
    Promotion,
    Favorite,
    Ingredients,
)
from .permissions import IsAdminOrReadOnly
from .filter import DrinkFilter
from .pagination import CustomMetaPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = Drinkserializers
    filterset_class = DrinkFilter
    pagination_class = CustomMetaPagination
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['name', 'category__name']
    ordering_fields = ['price', 'name']
    filterset_fields = ['category__id', 'price']

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
    permission_classes = [IsAdminOrReadOnly]

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


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = Reviewserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['rating', 'drink__id']
    pagination_class = CustomMetaPagination

    @action(detail=False, methods=['GET'])
    def top_review(self, request):
        review = Review.objects.filter(rating__gte=4).order_by('-rating')
        rwv = Reviewserializers(review, many=True)
        return Response(rwv.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        drink_pk = self.kwargs.get('drink_pk')
        if drink_pk:
            return Review.objects.filter(drink=drink_pk)
        return Review.objects.all()

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = Promotionserializers
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        drinks = serializer.validated_data.pop('drinks_ids')
        promotion = serializer.save()
        promotion.drinks.set(drinks)


class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = Favoriteserializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)


class IngredientsViewSet(viewsets.ModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = Ingredientsserializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        drinks = serializer.validated_data.pop('drinks_ids')
        ingredients = serializer.save()
        ingredients.drinks.set(drinks)
