""" Modelos Estanterias de Libros para Usuarios """
from django.db import models
from django.contrib.auth.models import User
from base_app.models import CustomModel


class Estante(CustomModel):
	""" Representa un Estante donde el usuario va
	guardando libros de diferentes categorias """
	nombre = models.CharField(
		verbose_name='Nombre',
		max_length=150,
		default='Estante',
		help_text='Nombre de la Estanteria',
	)
	private = models.BooleanField(
		verbose_name='Publico/Privado',
		default=True,
		help_text='Define si la estanteria solo lo puede ver el usuario',
	)
	created_by = models.ForeignKey(
        User,
        related_name='estanteria_creation',
        on_delete=models.DO_NOTHING,
    )
	updated_by = models.ForeignKey(
        User,
        related_name='estanteria_update',
        on_delete=models.DO_NOTHING,
        null=True,
    )
	
	def __str__(self):
		return self.nombre
