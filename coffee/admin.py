from django.contrib import admin
from .models import (
    Drink,
    Category,
    Order,
    OrderItem,
    Promotion,
    Review,
    Favorite,
    Ingredient,
)


admin.site.register(Drink)
admin.site.register(Category)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Promotion)
admin.site.register(Review)
admin.site.register(Ingredient)
admin.site.register(Favorite)
