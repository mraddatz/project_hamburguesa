from django.db import models
from django.core.validators import MinValueValidator


class Ingredient(models.Model):
    nombre = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=128)
    

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Burger(models.Model):
    nombre = models.CharField(max_length=128)
    precio = models.IntegerField(validators=[MinValueValidator(1)])
    descripcion = models.CharField(max_length=256)
    imagen = models.CharField(max_length=128)
    ingredientes = models.ManyToManyField('Ingredient', related_name='hamburguesas', blank=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre