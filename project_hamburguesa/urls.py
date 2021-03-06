"""project_hamburguesa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apiapp import views as apiviews
from register import views as registerviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registerviews.register, name="register"),
    path('', apiviews.index, name='index'),
    path('getbanks/', apiviews.banks, name='banks'),
    path('test/', apiviews.test, name='banks'),
    path('return/', apiviews.retorna, name='retorna'),
    path('api/', include('apiapp.api.urls', 'burger_api')),
    path('', include("django.contrib.auth.urls")),

]
