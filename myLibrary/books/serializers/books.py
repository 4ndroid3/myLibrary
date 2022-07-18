""" Serializadores de Libros y sus relaciones """

from rest_framework import serializers
from books.models.about_libros import Genero


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