""" Serializadores de Libros y sus relaciones """

from rest_framework import serializers

from books.models.about_libros import (
    Autor,
    Genero,
)
from books.models.libros import Libro


class GeneroSerializer(serializers.ModelSerializer):
    """ Serializador de Generos """
    class Meta:
        model = Genero
        fields = '__all__'


class GeneroSerializerMin(serializers.ModelSerializer):
    """ Serializador Anidado de Generos """
    url = serializers.HyperlinkedIdentityField(view_name='books-api:genero-detail')
    class Meta:
        model = Genero
        fields = (
            'url',
            'nombre',
        )

class AutorSerializer(serializers.ModelSerializer):
    """ Serializador de Generos """
    class Meta:
        model = Autor
        fields = '__all__'


class AutorSerializerMin(serializers.ModelSerializer):
    """ Serializador resumido de Generos """
    url = serializers.HyperlinkedIdentityField(view_name='books-api:autor-detail')
    pais = serializers.CharField(
        write_only=True,
        required=False,
    )
    class Meta:
        model = Autor
        fields = (
            'id',
            'url',
            'nombre',
            'apellido',
            'pais',
        )
    

class LibroSerializer(serializers.ModelSerializer):
    """ Serializador detallado de Libro """
    created_by = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    genero = serializers.SlugRelatedField(
        slug_field='nombre',
        many=True,
        read_only=True,
    )
    genero_id = serializers.PrimaryKeyRelatedField(
        source='genero',
        queryset=Genero.objects.all(),
        many=True,
        write_only=True,
    )
    autor = AutorSerializerMin(
        read_only=True,
    )
    autor_id = serializers.PrimaryKeyRelatedField(
        source='autor',
        queryset=Autor.objects.all(),
        write_only=True,
    )
    img_cover = serializers.CharField(
        required=False
    )
    # updated_by = 
    class Meta:
        model = Libro
        fields = '__all__'


class LibroSerializerMin(serializers.ModelSerializer):
    """ Serializador resumido de Libro """
    url = serializers.HyperlinkedIdentityField(view_name='books-api:libro-detail')
    autor = AutorSerializerMin(
        read_only=True,
    )
    class Meta:
        model = Libro
        fields = (
            'nombre',
            'url',
            'autor',
            'anio_publicacion',
        )