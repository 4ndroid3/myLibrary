""" Modelos de Libros """

from django.db import models
from django.contrib.auth.models import User

from base_app.models import CustomModel

class Libro(CustomModel):
    """ Modelo que representa un libro """
    created_by = models.ForeignKey(
        User,
        related_name='libro_creation',
        on_delete=models.DO_NOTHING,
    )
    updated_by = models.ForeignKey(
        User,
        related_name='libro_update',
        on_delete=models.DO_NOTHING,
        null=True,
    )
    nombre = models.CharField(
        null=False,
        verbose_name='Nombre',
        max_length=150,
        help_text="Nombre del libro",
    )
    anio_publicacion = models.IntegerField(
        null=True,
        blank=True,
        help_text="Año en que se publico el libro",
        verbose_name='Año Publicación',      
    )
    autor = models.ForeignKey(
        "books.Autor",
        related_name='autor_libro',
        on_delete=models.DO_NOTHING,
        null=True,
        help_text="Autor del libro"
    )
    hojas = models.IntegerField(
        null=True,
        blank=True,
        help_text="Cantidad de hojas del libro",
        verbose_name='Cantidad de Hojas',      
    )
    genero = models.ManyToManyField(
        "books.Genero",
        related_name='genero_libro',
        help_text="Genero Literario asociado al libro"
    )
    img_cover = models.CharField(
        null=False,
        verbose_name='Imagen',
        max_length=150,
        help_text="Imagen de Portada del Libro",
    )

    def __str__(self):
        try:
            return str(self.nombre) + ' | ' + str(self.autor.nombre) + ' ' + str(self.autor.apellido)
        except:
            return str(self.nombre)