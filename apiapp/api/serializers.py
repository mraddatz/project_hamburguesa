from rest_framework import serializers
from apiapp.models import Burger, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'description']

class CustomIngredientSerializer(IngredientSerializer):

    def to_representation(self, instance):
        data = super(IngredientSerializer, self).to_representation(instance)
        base_url = "http://localhost:8000/api/ingrediente/"
        path = base_url + str(data['id'])
        return { 'path' : path }


class BurgerSerializer(serializers.ModelSerializer):

    ingredients = CustomIngredientSerializer(many = True, required = False)

    class Meta:
        model = Burger
        fields = ['id', 'name', 'price', 'description', 'image', 'ingredients']



