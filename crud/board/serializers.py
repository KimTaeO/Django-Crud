from rest_framework import serializers
from .models import Board

class BoardSerializer(serializers.Serializer):
    model = Board
    fields = ('id', 'title', 'content')