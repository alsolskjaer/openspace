from rest_framework import serializers

from .models import ToDo


# Serializer yang menyamakan field model
class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'  # menampilkan semua field dari model ToDo
