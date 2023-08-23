from rest_framework import serializers
from .models import Usuarios

class UsuariosSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    altura = serializers.FloatField()
    peso = serializers.FloatField()

    def create(self, validated_data):
        return Usuarios.objects.create(**validated_data)

