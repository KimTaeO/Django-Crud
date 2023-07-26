from rest_framework import serializers
from .models import Board

class BoardSerializer(serializers.Serializer):
    class Meta:
        model = Board()
        fields = ['__all__']