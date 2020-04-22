from django.db import models
from django.core.validators import MinValueValidator


class Ingredient(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Burger(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    description = models.CharField(max_length=256)
    image = models.CharField(max_length=128)
    ingredients = models.ManyToManyField('Ingredient', related_name='hamburgers', blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name