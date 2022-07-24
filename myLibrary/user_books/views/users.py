""" Views de Libros Guardados """

from rest_framework.routers import APIRootView
from rest_framework import mixins
from rest_framework.viewsets import (
	GenericViewSet,
	ModelViewSet,
)
from user_books.models.libro_leido import LibroGuardado
from user_books.models.estanteria import Estante
from user_books.serializers import users


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
	serializer_class = users.EstanteriaSerializer


class LibrosLeidosView(ModelViewSet):
	""" 
	Viewset de los Libros Leidos o guardados
	permite `listar`, `crear`, `actualizar` y `elimnar` 
	"""
	queryset = LibroGuardado.objects.filter().order_by('-fecha_leido')
	serializer_class = users.LibroGuardadoSerializerMin

	serializer_action_classes = {
		'retrieve': users.LibroGuardadoSerializer,
		'create': users.LibroGuardadoSerializer
	}

	def get_serializer_class(self):
		try:
			return self.serializer_action_classes[self.action]
		except (KeyError, AttributeError):
			return super().get_serializer_class()

	def perform_create(self, serializer):
		serializer.save(created_by=self.request.user)