from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from apiapp.api import views


app_name = "APIHamburger"

urlpatterns = [
    path( 'hamburguesa', views.BurgerList.as_view()),
    path( 'hamburguesa/<int:pk>', views.BurgerDetail.as_view()),
    path( 'ingrediente', views.IngredientList.as_view()),
    path( 'ingrediente/<int:pk>', views.IngredientDetail.as_view()),
    path( 'hamburguesa/<int:burger_pk>/ingrediente/<int:ingredient_pk>', views.BurgerIngredientDetail.as_view()),
    path( 'notify', views.notify, name='notify')


]

urlpatterns = format_suffix_patterns(urlpatterns)
