""" serializadores de todo lo relacionado con los libros leidos """
from rest_framework import serializers

from user_books.models import Estante

class EstanteriaSerializer(serializers.ModelSerializer):
    """ Serializador de Estanteria """
    class Meta:
        model = Estante
        fields = '__all__'