from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        created = serializers.DateTimeField(read_only=True)