from django.contrib import admin
from .models.estanteria import Estante
from .models.libro_leido import LibroGuardado

admin.site.register(LibroGuardado)
admin.site.register(Estante)