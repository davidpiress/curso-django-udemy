from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    #title: Um CharField com um máximo de 65 caracteres, representando o título da receita.
    title = models.CharField(max_length=65)

    # description: Um CharField com um máximo de 165 caracteres, 
    # representando uma breve descrição da receita.
    description = models.CharField(max_length=165)

    # slug: Um SlugField, geralmente usado para criar URLs amigáveis para SEO. 
    # Geralmente é derivado do título.
    slug = models.SlugField()

    #preparation_time: Um IntegerField representando o tempo de preparação da receita.
    preparation_time = models.IntegerField()

    # preparation_time_unit: Um CharField com um máximo de 65 caracteres, 
    # representando a unidade do tempo de preparação (por exemplo, minutos, horas).
    preparation_time_unit = models.CharField(max_length=65)

    #servings: Um IntegerField representando o número de porções que a receita rende.
    servings = models.IntegerField()

    # servings_unit: Um CharField com um máximo de 65 caracteres, 
    #representando a unidade para as porções (por exemplo, pessoas, porções).
    servings_unit = models.CharField(max_length=65)

    #preparation_steps: Um TextField contendo os passos para preparar a receita.
    preparation_steps = models.TextField()

    #preparation_steps_is_html: Um BooleanField indicando se os passos de preparação contêm formatação HTML.
    preparation_steps_is_html = models.BooleanField(default=False)

    #created_at: Um DateTimeField que registra automaticamente 
    #a data e hora em que a instância da receita é criada.
    #data e hora
    created_at = models.DateTimeField(auto_now_add=True)

    #updated_at: Um DateTimeField que é atualizado automaticamente para a 
    #data e hora
    updated_at = models.DateTimeField(auto_now=True)

    #is_published: Um BooleanField indicando se a receita foi publicada.
    is_published = models.BooleanField(default=False)

    #cover: Um ImageField usado para fazer upload de uma imagem de capa para a receita. 
    #É armazenado no diretório especificado com um caminho dinâmico baseado na data de upload.
    #é um tipo de campo utilizado para representar campos de modelo que armazenam imagens. 
    #Este campo é usado quando você precisa armazenar arquivos de imagem em seu banco de dados.
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None,
    )

    author = models.ForeignKey( 
        User, on_delete=models.SET_NULL, null=True
    )
    
    def __str__(self):
        return self.title



# EDITED
# title description slug
# preparation_time preparation_time_unit
# servings servings_unit
# preparation_step
# preparation_step_is_html
# created_at updated_at
# is_published
# cover
# category (Relação)
# Author (Relação)