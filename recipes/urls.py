# urls.py dentro do aplicativo 'recipes'


from django.urls import path
from . import views

app_name = 'recipes'  # Definindo o namespace {% url recipes:recipe recipe.id %}

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/category/<int:category_id>/', views.category, name='category'),
    path('recipes/<int:id>/', views.recipe, name='recipe'),  # Exemplo de URL com namespace
    # outras URLs do seu aplicativo
]
