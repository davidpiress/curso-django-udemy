from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('recipes/3/', views.recipes),
    
]
