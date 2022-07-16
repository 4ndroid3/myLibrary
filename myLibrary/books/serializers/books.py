""" Serializadores de Libros y sus relaciones """

from rest_framework.serializers import ModelSerializer

from books.models.about_libros import Genero

class GeneroSerializer(ModelSerializer):
    """ Serializador de Generos """
    class Meta:
        model = Genero
        fields = '__all__'