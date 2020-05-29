from django.db import models
from django.db.models.signals import pre_save
from core.utils import save_slug, img_path





# https://trottospizza.com/product/supreme/
# pizza list
class Item(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=500, blank=True)
    img = models.FileField(upload_to=img_path, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    slices = models.IntegerField(default=6)
    slug = models.SlugField(max_length=72, unique=True, blank=True)
    ingredients = models.ManyToManyField('Ingredient', blank=True)


    def __str__(self):
        return self.name



pre_save.connect(save_slug, sender='item.Item')

class Ingredient(models.Model):
    name = models.CharField(max_length=120)
    quantity = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=72, unique=True, blank=True)

    def __str__(self):
        return self.name


pre_save.connect(save_slug, sender='item.Ingredient')
