from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.routers import APIRootView

from books.models.about_libros import Genero
from books.serializers.books import GeneroSerializer


class CircuitsRootView(APIRootView):
    """
    Books API root view
    """
    def get_view_name(self):
        return 'Books'

# Create your views here.
class GenerosView(ModelViewSet):
    """ ViewSet de los generos,
    permite listar, crear y actualizar"""
    queryset = Genero.objects.filter().order_by('-nombre')
    serializer_class = GeneroSerializer