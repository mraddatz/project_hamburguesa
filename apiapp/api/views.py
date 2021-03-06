from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from apiapp.models import Burger, Ingredient
from rest_framework import generics
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt



from apiapp.api.serializers import BurgerSerializer, IngredientSerializer


@csrf_exempt
@api_view(['POST'])
def notify(request):
    print("Llego request de notify")
    print(request)
    print(type(request))
    print(request.data)
    return Response(status=status.HTTP_200_OK)




class BurgerList(APIView):
    """
    List all burgers, or create a new snippet.
    """
    def get(self, request, format=None):
        burgers = Burger.objects.all()
        serializer =  BurgerSerializer(burgers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BurgerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BurgerDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Burger.objects.get(pk=pk)
        except Burger.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        burger = self.get_object(pk)
        serializer = BurgerSerializer(burger)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        burger = self.get_object(pk)
        serializer = BurgerSerializer(burger, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            burger = self.get_object(pk)
            burger.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            Response(status=status.HTTP_404_NOT_FOUND)

class IngredientList(APIView):
    """
    List all burgers, or create a new burger.
    """
    def get(self, request, format=None):
        print("Entro a Get")
        ingredients = Ingredient.objects.all()
        serializer =  IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IngredientDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        print("Entro a get specific")
        try:
            return Ingredient.objects.get(pk=pk)
        except Ingredient.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ingredient = self.get_object(pk)
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        ingredient = self.get_object(pk)
        serializer = IngredientSerializer(ingredient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            ingredient = self.get_object(pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if (ingredient.hamburguesas.all()):
            return Response(status=status.HTTP_409_CONFLICT)
        try:
            ingredient.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

# class BurgerList(generics.ListCreateAPIView):
#     queryset = Burger.objects.all()
#     serializer_class = BurgerSerializer


# class BurgerDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Burger.objects.all()
#     serializer_class = BurgerSerializer

# class IngredientList(generics.ListCreateAPIView):
#     queryset = Ingredient.objects.all()
#     serializer_class = IngredientSerializer


# class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Ingredient.objects.all()
#     serializer_class = IngredientSerializer


class BurgerIngredientDetail(APIView): 
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_burger(self, burger_pk):
        try:
            return Burger.objects.get(pk=burger_pk)
        except Burger.DoesNotExist:
            raise Http400

    def get_ingredient(self, ingredient_pk):
        try:
            return Ingredient.objects.get(pk=ingredient_pk)
        except burger.DoesNotExist:
            raise Http404

    def put(self, request, burger_pk, ingredient_pk, format=None):
        print("Entro a PUT")
        try:
            burger = self.get_burger(burger_pk)
            print("Encontro Burger")
            ingredient = self.get_ingredient(ingredient_pk)
            print("Encontro Ingredient")
            burger.ingredientes.add(ingredient)
            print("Asocio Ingredient Con hamburguesa")
            return Response(status=status.HTTP_201_CREATED)
        except:
            print("Va a retornar 400 Bad Request")
            return Response(status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, burger_pk, ingredient_pk, format=None):
        try:
            burger = self.get_burger(burger_pk)
            ingredient = self.get_ingredient(ingredient_pk)
            if ingredient not in burger.ingredientes.all():
                return Response(status=status.HTTP_404_NOT_FOUND)
            burger.ingredientes.remove(ingredient)
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)