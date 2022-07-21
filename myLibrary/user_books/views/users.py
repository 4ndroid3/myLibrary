from django.shortcuts import render

from rest_framework.routers import APIRootView
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from user_books.models.estanteria import Estante
from user_books.serializers import EstanteriaSerializer

# Create your views here.


class UserBooksRootView(APIRootView):
	"""
	Books API root view
	"""

	def get_view_name(self):
		return 'User Books'


class EstanteriaView(mixins.CreateModelMixin,
				  mixins.RetrieveModelMixin,
				  mixins.UpdateModelMixin,
				  mixins.ListModelMixin,
				  GenericViewSet):
	"""
	ViewSet de los Estanterias,
	permite `listar`, `crear` y `actualizar`
	"""
	queryset = Estante.objects.filter()
	serializer_class = EstanteriaSerializer