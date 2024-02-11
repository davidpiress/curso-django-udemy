from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={'name': 'davi',})

def recipes(request):
    return render(request, 'recipes/pages/recipe_view.html', context={'name': 'davi',})
