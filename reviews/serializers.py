from rest_framework import serializers
from .models import MediaItem

class MediaItemSerializer(serializers.ModelSerializer):
    # This class converts MediaItem models to JSON format
    class Meta:
        model = MediaItem
        fields = ['id', 'title', 'category', 'author_or_director', 'description']