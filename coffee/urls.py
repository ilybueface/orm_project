from coffee.views import drink_list, category, drink_detail, order_list, order_detail
from django.urls import path


urlpatterns = [
    path('drinks/', drink_list),
    path('category/', category),
    path('drinks/<int:pk>/', drink_detail),
    path('orders/', order_list),
    path('orders/<int:pk>/', order_detail)
]
