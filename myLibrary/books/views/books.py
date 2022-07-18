from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.routers import APIRootView

from books.models.about_libros import Genero
from books.serializers.books import GeneroSerializer, GeneroSerializerMin


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
    queryset = Genero.objects.filter().order_by('-nombre')
    serializer_class = GeneroSerializerMin
    serializer_action_classes = {
        'retrieve': GeneroSerializer
    }

    def get_serializer_class(self):
        try:
            self.serializer_action_classes
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
    pass