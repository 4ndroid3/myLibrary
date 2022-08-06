""" Vistas de Libros y sus relaciones """

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.routers import APIRootView
from django_filters import rest_framework as filters

from books.models import (
    Autor,
    Genero,
)
from books.serializers import books
from books.models import Libro
from books.filters import AutorsFilter, BooksFilter


class BooksRootView(APIRootView):
    """
    Books API root view
    """
    def get_view_name(self):
        return 'Books'

# Create your views here.
class GenerosView(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    """ ViewSet de los generos,
    permite `listar`, `crear` y `actualizar`"""
    queryset = Genero.objects.filter().order_by('nombre')
    serializer_class = books.GeneroSerializerMin
    serializer_action_classes = {
        'retrieve': books.GeneroSerializer
    }

    def get_serializer_class(self):
        try:
            # self.serializer_action_classes
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

class AutoresView(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    """ ViewSet de los Autores,
    permite `listar`, `crear`, `eliminar` y `actualizar` """

    queryset = Autor.objects.filter().order_by('apellido')
    serializer_class = books.AutorSerializerMin
    serializer_action_classes = {
        'retrieve': books.AutorSerializer
    }
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AutorsFilter

    def get_serializer_class(self):
        try:
            self.serializer_action_classes
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()


class LibrosView(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    """ ViewSet de los Autores,
    permite `listar`, `crear`, `eliminar` y `actualizar`   """
    queryset = Libro.objects.filter().order_by('autor')
    serializer_class = books.LibroSerializerMin
    serializer_action_classes = {
        'retrieve': books.LibroSerializer,
        'create': books.LibroSerializer
    }
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BooksFilter

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()
    
    def perform_create(self, serializer):
        if self.request.user.id:
            serializer.save(created_by=self.request.user)
        else:
            serializer.save()