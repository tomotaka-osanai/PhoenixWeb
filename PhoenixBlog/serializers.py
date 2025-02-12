from rest_framework import serializers
from .models import PhoenixBlog


class PhoenixBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoenixBlog
        fields = ('id', 'title', 'description', 'completed')
