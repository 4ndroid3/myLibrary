from django.contrib import admin

from books.models.libros import Libro
from books.models.about_libros import Genero

# Register your models here.
admin.site.register(Libro)
admin.site.register(Genero)