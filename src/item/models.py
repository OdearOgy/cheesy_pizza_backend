from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    ingredients = models.ManyToManyField(
        'Ingredient', blank=True)


    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=120)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
