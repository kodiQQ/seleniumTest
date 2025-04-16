from django.urls import path, include
from .views import runSelenium

urlpatterns = [

    path('runselenium/', runSelenium, name='selenium'),




]
