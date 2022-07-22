""" Modelos de Libros guardados y leidos """
from base_app.models import CustomModel
from django.db import models
from django.contrib.auth.models import User

class LibroGuardado(CustomModel):
    """ Modelo que representa un libro
    guardado por un usuario, puede ser leido o no. """

    libro = models.ForeignKey(
        "books.Libro",
        on_delete=models.DO_NOTHING,
        related_name="libro_libro_leido",
        help_text="Libro guardado por un usuario",
        null=False,
    )
    fecha_leido = models.DateField(
        null=True,
        blank=True,
        help_text="Fecha en la que se leyo el libro"
    )
    leido = models.BooleanField(
        default=False,
        help_text="Decreta si el libro se leyo o solo se almaceno.",
        null=False,
    )
    estante = models.ForeignKey(
        "user_books.Estante",
        on_delete=models.DO_NOTHING,
        related_name="estante_libro_leido",
        help_text="Estante donde está guardado el libro",
        null=True,
        blank=True,
    )
    created_by = models.ForeignKey(
        User,
        related_name='libro_leido_creation',
        on_delete=models.DO_NOTHING,
    )
    updated_by = models.ForeignKey(
        User,
        related_name='libro_leido_update',
        on_delete=models.DO_NOTHING,
        null=True,
    )

    def __str__(self):
        try:
            return str(self.libro.nombre) + ' | ' + str(self.fecha_leido)
        except Exception:
            return 'Libro Leido'