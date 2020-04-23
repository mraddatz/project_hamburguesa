from django.urls import path
from apiapp.api.views import burgerview, ingredientview
from django.conf.urls import url


app_name = "APIHamburger"

urlpatterns = [
    path( 'hamburguesa/', burgerview.as_view()),
    path( 'ingrediente/', ingredientview.as_view()),
]