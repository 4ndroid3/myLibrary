""" Filtros correspondientes a los libros leidos """
from django_filters import rest_framework as filters

from user_books.models.libro_leido import LibroGuardado

class MyBooksFilter(filters.FilterSet):
    """ Filtra libros leidos por un usuario """
    nombre = filters.CharFilter(field_name='libro__nombre', lookup_expr='icontains')
    fecha_leido_mayor = filters.DateFilter(field_name='fecha_leido', lookup_expr='gte')
    fecha_leido_menor = filters.DateFilter(field_name='fecha_leido', lookup_expr='lte')
    class Meta:
        model = LibroGuardado
        fields = ''