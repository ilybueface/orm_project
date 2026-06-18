from coffee.views import (
    DrinkViewSet,
    OrderViewSet,
    CategoryViewSet,
    ReviewViewSet,
    PromotionViewSet,
    FavoriteViewSet,
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'drinks', DrinkViewSet, basename='Drink')
router.register(r'order', OrderViewSet, basename='Order')
router.register(r'category', CategoryViewSet, basename='Category')
router.register(r'review', ReviewViewSet, basename='Review')
router.register(r'promotion', PromotionViewSet, basename='Promotion')
router.register(r'favorite', FavoriteViewSet, basename='Favorite')


urlpatterns = router.urls
