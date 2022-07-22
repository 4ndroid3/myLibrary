""" Modelos para los generos """
from django.db import models
from base_app.models import CustomModel

class Genero(CustomModel):
    """ Modelo que representa un genero """
    nombre = models.CharField(
        verbose_name="Nombre",
        max_length=150,
        help_text="Genero Literario",
        null=False,
    )

    def __str__(self):
        return self.nombre


class Autor(CustomModel):
    """ Modelo que representa a un Autor de libros """
    nombre = models.CharField(
        verbose_name="Nombre",
        max_length=150,
        help_text="Nombre del Autor del Libro",
        null=False,
    )
    apellido = models.CharField(
        verbose_name="Apellido",
        max_length=150,
        help_text="Apellido del Autor del Libro",
        null=False,
    )
    pais = models.CharField(
        verbose_name="País",
        max_length=150,
        help_text="País nacimiento del Autor",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.nombre + self.apellido
