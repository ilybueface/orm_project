from coffee.views import (
    DrinkViewSet,
    OrderViewSet,
    CategoryViewSet,
    ReviewViewSet,
    PromotionViewSet,
    FavoriteViewSet,
    IngredientsViewSet,
)
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register(r'drinks', DrinkViewSet, basename='Drink')
drinks_router = routers.NestedDefaultRouter(router, r'drinks', lookup='drink')
drinks_router.register(r'reviews', ReviewViewSet, basename='drink-reviews')
router.register(r'order', OrderViewSet, basename='Order')
router.register(r'category', CategoryViewSet, basename='Category')
router.register(r'review', ReviewViewSet, basename='Review')
router.register(r'promotion', PromotionViewSet, basename='Promotion')
router.register(r'favorite', FavoriteViewSet, basename='Favorite')
router.register(r'ingredient', IngredientsViewSet, basename='Ingredient')


urlpatterns = router.urls + drinks_router.urls
