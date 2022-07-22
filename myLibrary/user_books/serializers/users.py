""" serializadores de todo lo relacionado con los libros leidos """
from rest_framework import serializers
from books.models.libros import Libro
from books.serializers.books import LibroSerializerMin
from user_books.models.libro_leido import LibroGuardado

from user_books.models import Estante

class EstanteriaSerializer(serializers.ModelSerializer):
    """ Serializador de Estanteria """
    class Meta:
        model = Estante
        fields = '__all__'

class EstanteriaSerializerMin(serializers.ModelSerializer):
    """ Serializador de Estanteria Min """
    url = serializers.HyperlinkedIdentityField(view_name='user_books-api:estante-detail')
    class Meta:
        model = Estante
        fields = (
            'id',
            'url',
            'nombre',
        )
    

class LibroGuardadoSerializer(serializers.ModelSerializer):
    """ Serializador de LibrosGuardados """
    created_by = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    libro = LibroSerializerMin(
        read_only=True
    )
    libro_id = serializers.PrimaryKeyRelatedField(
        source='libro',
        queryset=Libro.objects.all(),
        write_only=True
    )
    estante = EstanteriaSerializerMin(
        read_only=True
    )
    estante_id = serializers.PrimaryKeyRelatedField(
        source='estante',
        queryset=Estante.objects.all(),
        write_only=True
    )
    class Meta:
        model = LibroGuardado
        fields = '__all__'


class LibroGuardadoSerializerMin(serializers.ModelSerializer):
    """ Serializador de Libros guardados min """
    url = serializers.HyperlinkedIdentityField(view_name='user_books-api:libroguardado-detail')
    libro = LibroSerializerMin(
        read_only=True
    )
    class Meta:
        model = LibroGuardado
        fields = (
            'id',
            'url',
            'libro',
            'fecha_leido',
        )