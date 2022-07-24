from dataclasses import field
from django_filters import rest_framework as filters
from books.models import Libro
from django.db.models import Q



class BooksFilter(filters.FilterSet):
    """ filtros para la view de Libros"""
    nombre = filters.CharFilter(field_name='nombre', lookup_expr='icontains')
    anio_publicacion = filters.NumberFilter(field_name='anio_publicacion', lookup_expr='exact')
    anio_publicacion_gte = filters.NumberFilter(field_name='anio_publicacion', lookup_expr='gte')
    anio_publicacion_lte = filters.NumberFilter(field_name='anio_publicacion', lookup_expr='lte')
    hojas_gte = filters.NumberFilter(field_name='hojas', lookup_expr='gte')
    hojas_lte = filters.NumberFilter(field_name='hojas', lookup_expr='lte')
    # autor = filters.CharFilter(
    #     method='filter_author',
    #     label="filtro por nombre o apellido del autor",
    # )
    autor_nombre = filters.CharFilter(field_name='autor__nombre', lookup_expr='icontains')
    autor_apellido = filters.CharFilter(field_name='autor__apellido', lookup_expr='icontains')
    autor_pais = filters.CharFilter(field_name='autor__pais', lookup_expr='icontains')
    generos = filters.CharFilter(field_name='genero__nombre', lookup_expr="icontains")

    class Meta:
        model = Libro
        fields = '__all__'
    
    # def filter_author(self, queryset, name, value):
    #     """ filtro para autor """
    #     autor = self.request.query_params.get('autor', None)
    #     if autor is not None:
    #         queryset = queryset.filter(
    #             Q(autor__nombre__icontains=autor) |
    #             Q(autor__apellido__icontains=autor)
    #         )
    #     return queryset