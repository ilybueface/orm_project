from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.price} {self.category}"


class Order(models.Model):
    date = models.DateField()
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.drink} {self.date}"


class Review(models.Model):
    drink = models.ForeignKey(
        Drink,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
            User,
            on_delete=models.SET_NULL,
            null=True,
            blank=True,
    )
    text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.drink} {self.rating}"


class Promotion(models.Model):
    title = models.CharField(max_length=300)
    discount_percent = models.IntegerField()
    active_until = models.DateField()
    drinks = models.ManyToManyField(Drink)

    def __str__(self):
        return f"{self.title} {self.discount_percent}"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.drink}"


class Ingredients(models.Model):
    name = models.CharField(max_length=200)
    is_allergen = models.BooleanField()
    extra_price = models.IntegerField()
    drinks = models.ManyToManyField(Drink)

    def __str__(self):
        return f"{self.name} {self.is_allergen} {self.extra_price}"
