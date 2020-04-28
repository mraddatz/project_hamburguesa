from rest_framework import serializers
from apiapp.models import Burger, Ingredient



class BurgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burger
        fields = ['id', 'name', 'price', 'description', 'image', 'ingredients']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'description']