from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def index(request):
    print("Entered index")
    my_variable = os.environ.get('ENV_VARIABLE')
    string = "Welcome to Hamburger API Homepage. Here will be the documentation + "
    string_env = string + my_variable
    return HttpResponse(string_env)


