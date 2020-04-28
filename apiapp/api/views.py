from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from apiapp.models import Burger, Ingredient
from rest_framework import generics


from apiapp.api.serializers import BurgerSerializer, IngredientSerializer

class BurgerList(generics.ListCreateAPIView):
    queryset = Burger.objects.all()
    serializer_class = BurgerSerializer


class BurgerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Burger.objects.all()
    serializer_class = BurgerSerializer

class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class BurgerIngredientDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_burger(self, burger_pk):
        try:
            return Burger.objects.get(pk=burger_pk)
        except Snippet.DoesNotExist:
            raise Http400

    def get_ingredient(self, ingredient_pk):
        try:
            return Ingredient.objects.get(pk=ingredient_pk)
        except Snippet.DoesNotExist:
            raise Http404

    def put(self, request, burger_pk, ingredient_pk, format=None):
        print("Entro a put BurgerIngredient")
        print("Burger ID: ", burger_pk)
        print("Ingredient ID: ", ingredient_pk)
        try:
            burger = self.get_burger(burger_pk)
            ingredient = self.get_ingredient(ingredient_pk)
            burger.ingredients.add(ingredient)
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, burger_pk, ingredient_pk, format=None):
        print("Entro a DELETE BurgerIngredient")
        print("Burger ID: ", burger_pk)
        print("Ingredient ID: ", ingredient_pk)
        try:
            burger = self.get_burger(burger_pk)
            ingredient = self.get_ingredient(ingredient_pk)
            burger.ingredients.remove(ingredient)
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)