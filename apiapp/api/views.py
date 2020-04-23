from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from apiapp.models import Burger, Ingredient

from apiapp.api.serializers import BurgerSerializer, IngredientSerializer

class burgerview(APIView):
    def get(self, request):
        hamburguesas = Burger.objects.all()
        serializer = BurgerSerializer(hamburguesas, context={'request': request}  , many=True)
        return Response(serializer.data)

class ingredientview(APIView):
    def get(self, request):
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, context={'request': request}  , many=True)
        return Response(serializer.data)